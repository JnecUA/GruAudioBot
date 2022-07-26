from aiogram import Bot, Dispatcher, types
from handlers.handler import AbstractHandler
from services.service import Services
from handlers import keyboards as kb


class SelectStretchHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['wide_putin:select_stretch'])
        async def select_stretch(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'select_stretch')
            await self.answer(call, 'Выбери степень растяжения', kb.select_stretch())
