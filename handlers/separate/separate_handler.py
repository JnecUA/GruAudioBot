import os
import shutil
from aiogram import Bot, Dispatcher, types
from handlers.filters.action_filter import ActionFilter
from handlers.filters.payment_filter import PaymentFilter
from handlers.handler import AbstractHandler
from media_core.separate import Separate
from services.service import Services
from handlers import keyboards as kb


class SeparateHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(regexp='separate:\dstems')
        async def separate(call: types.CallbackQuery):
            stems = call.data[-6:]
            await self.userService.set_action(call.message.chat.id, f'separate:{stems}')
            await self.answer(call, 'Скинь мне аудио для разделения', kb.back('separate:select'))

        @self.dp.message_handler(ActionFilter('separate:\dstems'), PaymentFilter('separate'), content_types=['audio'])
        async def separate_create(message: types.Message):
            action = await self.userService.get_action(message.chat.id)
            stems = action[-6:]
            wait_message = await message.answer('Обрабатываю...')
            file_path = await self.file_download(message.audio.file_id, 'mp3', 'separate')
            output_path = await Separate().create(file_path, stems)
            shutil.make_archive(output_path, 'zip', output_path)
            await self.bot.send_document(message.chat.id, open(output_path + '.zip', 'rb'))
            await self.bot.delete_message(message.chat.id, wait_message.message_id)
            await message.delete()
            os.remove(file_path)
            shutil.rmtree(output_path)
            os.remove(output_path + '.zip')
