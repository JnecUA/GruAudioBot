import os
from aiogram import Bot, Dispatcher, types
from handlers.filters.action_filter import ActionFilter
from handlers.handler import AbstractHandler
from media_core.memes import WidePutin
from services.service import Services
from handlers import keyboards as kb


class WidePutinHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(regexp='wide_putin:\d')
        async def wide_putin(call: types.CallbackQuery):
            ratio = call.data[-1]
            await self.userService.set_action(call.message.chat.id, f'wide_putin:{ratio}')
            await self.answer(call, 'Скинь мне видео и я сделаю из тебя Путина!', kb.back('wide_putin:select_stretch'))

        @self.dp.message_handler(ActionFilter('wide_putin:\d'), content_types=['video'])
        async def wide_putin_create(message: types.Message):
            action = await self.userService.get_action(message.chat.id)
            ratio = int(action[-1])
            wait_message = await message.answer('Обрабатываю...')
            file_path = await self.file_download(message.video.file_id, 'mp4', 'memes')
            output_path = await WidePutin().create(file_path, ratio)
            await self.bot.send_video(message.chat.id, open(output_path, 'rb'))
            await self.bot.delete_message(message.chat.id, wait_message.message_id)
            await message.delete()
            os.remove(file_path)
            os.remove(output_path)
