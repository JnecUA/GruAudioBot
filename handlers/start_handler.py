import os
from handlers.filters.action_filter import ActionFilter
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

        @self.dp.message_handler(ActionFilter('profile'), content_types=["voice"])
        async def voice_download(message: types.Message):
            file_path = await self.file_download(message.voice.file_id, 'wav')
            await self.bot.send_voice(message.chat.id, open(file_path, 'rb'))
            os.remove(file_path)
            await message.answer('Nice voice')

        @self.dp.pre_checkout_query_handler(lambda query: True)
        async def checkout(pre_checkout_query: types.PreCheckoutQuery):
            await self.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

        @self.dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
        async def got_payment(message: types.Message):
            await self.bot.send_message(message.chat.id,
                                        f'<b>Оплата успешно произведена</b>', parse_mode='HTML')
