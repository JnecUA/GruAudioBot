import re
from aiogram import types
from handlers.filters.abstract_filter import AbstractFilter


class ActionFilter(AbstractFilter):
    def __init__(self, action: str) -> None:
        super().__init__()
        self.action = action
        self.userService = self.services.userService

    async def check(self, message: types.Message) -> bool:
        user = await self.userService.get_user(chat_id=message.chat.id)
        return re.match(self.action, user['action'])
