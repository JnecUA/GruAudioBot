from aiogram import Bot, Dispatcher, types
from handlers.handler import AbstractHandler
from services.service import Services
from handlers import keybords as kb


class CreateMemeHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['create_meme'])
        async def create_meme(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'create_meme')
            await self.answer(call, 'Выбери мем для создания', kb.create_meme())
