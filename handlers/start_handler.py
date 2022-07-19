from handlers.handler import AbstractHandler
from aiogram import types

class StartHandler(AbstractHandler):
    def wrap(self) -> None:
        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            await message.answer('Сосать бояться')