from abc import ABCMeta
from typing import Union
from aiogram import types

from aiogram import Bot, Dispatcher
from services.service import Services


class AbstractHandler:
    __metaclass__ = ABCMeta

    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        self.bot = bot
        self.dp = dp
        self.services = services
        self.wrap()

    async def answer(self, call: types.CallbackQuery, text: str, reply_markup: Union[types.InlineKeyboardMarkup, None] = None) -> None:
        try:
            await call.message.edit_text(text)
            await call.message.edit_reply_markup(reply_markup)
        except:
            pass

    async def file_download(self, file_id: str, extension: str, path_ending: str = '') -> str:
        file = await self.bot.get_file(file_id)
        file_path = f'static/{path_ending}/{file.file_unique_id}.{extension}'
        await self.bot.download_file(file.file_path, file_path)
        return file_path

    def wrap(self) -> None:
        pass
