from datetime import datetime
from typing import Union
from services.abstract_service import AbstractService

class UserService(AbstractService):
    def create_user(self, username: Union[str, None], chat_id: Union[int, None]):
        user = self.get_user(chat_id=chat_id)
        if (not user):
            _id = self.model.insert_one({
                'username': username,
                'chat_id': chat_id,
                'created_at': datetime.now(),
            }).inserted_id
            user = self.get_user(chat_id=chat_id)
        return user

    def get_user(self, *, chat_id: Union[int, None] = None, _id: Union[str, None] = None, username: Union[str, None] = None):
        query = self.create_simple_query(locals())
        return self.model.find_one(query)