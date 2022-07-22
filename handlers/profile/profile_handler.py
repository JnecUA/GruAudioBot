from aiogram import Bot, Dispatcher, types
from handlers.handler import AbstractHandler
from services.service import Services
from handlers import keybords as kb


class ProfileHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['profile'])
        async def profile(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'profile')
            await self.answer(call, 'Отправь мне голосовое сообщение и я улучшу его.\n\nИли выбери одну из функций и забавляйся', kb.profile())
