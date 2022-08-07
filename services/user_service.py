from datetime import datetime
from typing import Dict, Union
from services.abstract_service import AbstractService


class UserService(AbstractService):
    async def create_user(self, username: Union[str, None], chat_id: Union[int, None]):
        user = await self.get_user(chat_id=chat_id)
        if (not user):
            await self.model.insert_one({
                'username': username,
                'chat_id': chat_id,
                'action': '',
                'payments': {},
                'created_at': datetime.now(),
            })
            user = await self.get_user(chat_id=chat_id)
        return user

    async def get_user(self, *, chat_id: Union[int, None] = None, _id: Union[str, None] = None, username: Union[str, None] = None):
        query = self.create_simple_query(locals())
        return await self.model.find_one(query)

    async def update_payments(self, chat_id: int, payments: Dict[str, any]):
        await self.model.update_one({"chat_id": chat_id}, {"$set": {"payments": payments}})

    async def get_action(self, chat_id: int):
        user = await self.get_user(chat_id=chat_id)
        return user.get('action', '')

    async def set_action(self, chat_id: int, action: str):
        await self.model.update_one({"chat_id": chat_id}, {"$set": {"action": action}})
