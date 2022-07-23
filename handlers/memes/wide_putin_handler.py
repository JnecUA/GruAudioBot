import os
from aiogram import Bot, Dispatcher, types
from handlers.filters.action_filter import ActionFilter
from handlers.handler import AbstractHandler
from media_core.memes import WidePutin
from services.service import Services
from handlers import keybords as kb


class WidePutinHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.callback_query_handler(text=['wide_putin'])
        async def wide_putin(call: types.CallbackQuery):
            await self.userService.set_action(call.message.chat.id, 'wide_putin')
            await self.answer(call, 'Скинь мне видео и я сделаю из тебя Путина!', kb.back('create_meme'))

        @self.dp.message_handler(ActionFilter('wide_putin'), content_types=['video'])
        async def wide_putin_create(message: types.Message):
            wait_message = await message.answer('Обрабатываю...')
            file_path = await self.file_download(message.video.file_id, 'mp4')
            output_path = await WidePutin().create(file_path)
            await self.bot.send_video(message.chat.id, open(output_path, 'rb'))
            await self.bot.delete_message(message.chat.id, wait_message.message_id)
            await message.delete()
            os.remove(output_path)
