import os
from handlers.handler import AbstractHandler
from aiogram import Bot, Dispatcher, types

from services.service import Services


class StartHandler(AbstractHandler):
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        super().__init__(bot, dp, services)
        self.userService = self.services.userService

    def wrap(self) -> None:
        @self.dp.message_handler(commands=['start'])
        async def start(message: types.Message):
            user = self.userService.create_user(
                username=message.from_user.username, chat_id=message.chat.id)
            await message.answer(f'Сосать бояться sex={user}')

        @self.dp.message_handler(content_types=["voice"])
        async def voice_download(message: types.Message):
            file_path = await self.file_download(message.voice.file_id, 'mp3')
            await self.bot.send_voice(message.chat.id, open(file_path, 'rb'))
            os.remove(file_path)
            await message.answer('Nice voice')

        @self.dp.message_handler(content_types=["video"])
        async def video_download(message: types.Message):
            file_path = await self.file_download(message.video.file_id, 'mp4')
            await self.bot.send_video(message.chat.id, open(file_path, 'rb'))
            os.remove(file_path)
            await message.answer('Nice video')
