from datetime import datetime, time
import math
from typing import Union
from handlers.handler import AbstractHandler
from aiogram import Bot, Dispatcher, types
from services.service import Services
from handlers import keyboards as kb


class PaymentsHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        self.userService = services.userService
        super().__init__(bot, dp, services)

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text='payments')
        async def payments(call: types.CallbackQuery):
            user = await self.userService.get_user(chat_id=call.message.chat.id)
            payments = await make_payments_list(user)

            await self.userService.set_action(call.message.chat.id, f'payments:{call.message.message_id}')
            await self.answer(call, f'Здесь ты можешь оплатить необходимые тебе подписки\n\nВаши подписки:\n{payments}', kb.payments())

        @self.dp.pre_checkout_query_handler(lambda query: True)
        async def checkout(pre_checkout_query: types.PreCheckoutQuery):
            await self.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

        @self.dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
        async def got_payment(message: types.Message):
            user = await self.userService.get_user(chat_id=message.chat.id)
            payments = user['payments']
            active_payments = message.successful_payment.invoice_payload
            for payment in active_payments.split(' '):
                payments[payment] = datetime.now()
            await self.userService.update_payments(message.chat.id, payments)

            await message.answer('<b>Оплата успешно произведена</b>', parse_mode='HTML', reply_markup=kb.back('payments'))
            await self.bot.delete_message(user['chat_id'], user['action'].split(':')[1])

        async def make_payments_list(user) -> str:
            possible_payments = {
                "normalize_voice": "Нормализация ГС",
                "separate": "Разделение звука",
                "create_memes": "Создание мемов"
            }
            payments = user['payments']
            payments_new = payments.copy()
            for key, value in payments.items():
                if int(days_left(value).split(' ')[1]) < 0:
                    del payments_new[key]

            payments_list = ''
            for key, value in possible_payments.items():
                payments_list += f'{value}: {days_left(payments_new.get(key, "не активна"))}\n'
            await self.userService.update_payments(user['chat_id'], payments_new)
            return payments_list

        def days_left(time: Union[str, time]) -> str:
            if time == 'не активна':
                return time
            time = str(time)
            last_pay = datetime.fromisoformat(time)
            date_now = datetime.now()
            days_past = (date_now - last_pay).total_seconds() // (3600 * 24)
            days_left = 'осталось ' + str(30 - math.trunc(days_past)) + ' дней'
            return days_left
