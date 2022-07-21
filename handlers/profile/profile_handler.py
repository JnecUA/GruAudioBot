from aiogram import types 
from handlers.handler import AbstractHandler
from handlers import keybords as kb

class ProfileHandler(AbstractHandler):
    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['profile'])
        async def profile(call: types.CallbackQuery):
            await self.answer(call, 'Отправь мне голосовое сообщение и я улучшу его.\n\nИли выбери одну из функций и забавляйся', kb.profile())