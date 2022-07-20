from handlers.handler import AbstractHandler
from aiogram import Dispatcher, types

from services.service import Services

class StartHandler(AbstractHandler):
    def __init__(self, dp: Dispatcher, services: Services) -> None:
        super().__init__(dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            user = self.userService.create_user(username=message.from_user.username, chat_id=message.chat.id)
            await message.answer(f'Сосать бояться sex={user}')