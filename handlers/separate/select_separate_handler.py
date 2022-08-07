from aiogram import Bot, Dispatcher, types
from handlers.handler import AbstractHandler
from services.service import Services
from handlers import keyboards as kb


class SelectSeparateHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['separate:select'])
        async def select_separate(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'select_separate')
            await self.answer(call, 'Выбери категорию разделения:\n\n2stems - Вокал/Фон\n4stems - Вокал/Барабаны/Басс/Фон\n5stems - Вокал/Барабаны/Басс/Пианино/Фон', kb.select_separate())
