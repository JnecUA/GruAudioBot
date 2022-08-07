from handlers.handler import AbstractHandler
from aiogram import Bot, Dispatcher, types
from services.service import Services
from handlers import keyboards as kb


class StartHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        self.userService = services.userService
        super().__init__(bot, dp, services)

    def wrap(self) -> None:
        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            await self.userService.create_user(
                username=message.from_user.username,
                chat_id=message.chat.id
            )
            await self.userService.set_action(message.chat.id, 'start')
            await message.answer(f'Привет, я помогу сделать твои голосовые сообщение исключительно чистыми.\n\nЕщё я умею разделять музыку на дорожки вокал/барабаны/басс/другое и делать мемы. Хочешь попробовать?', reply_markup=kb.start())
