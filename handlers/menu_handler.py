from aiogram import Bot, Dispatcher, types
from handlers.handler import AbstractHandler
from services.service import Services
from handlers import keyboards as kb


class MenuHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['menu'])
        async def menu(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'menu')
            await self.answer(call, 'Отправь мне голосовое сообщение и я улучшу его.\n\nИли выбери одну из функций и забавляйся', kb.menu())
