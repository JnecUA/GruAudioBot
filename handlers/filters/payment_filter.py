from datetime import datetime
from aiogram import types
from handlers.filters.abstract_filter import AbstractFilter
from handlers import keyboards as kb


class PaymentFilter(AbstractFilter):
    def __init__(self, payment: str) -> None:
        super().__init__()
        self.payment = payment
        self.userService = self.services.userService

    async def check(self, message: types.Message) -> bool:
        user = await self.userService.get_user(chat_id=message.chat.id)
        last_payment = user['payments'].get(self.payment, None)
        if last_payment:
            payment_time_left = datetime.now() - datetime.fromisoformat(str(last_payment))
            payment_ended = payment_time_left.total_seconds() // (3600 * 24) > 30
        if last_payment is None or payment_ended:
            await message.delete()
            await message.answer('Кажется, ваша подписка закончилась 😔\nПродлите её в главном меню', reply_markup=kb.back('menu'))
            return False
        return True
