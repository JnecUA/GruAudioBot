from abc import ABCMeta

from aiogram import Bot, Dispatcher
from services.service import Services


class AbstractHandler:
    __metaclass__ = ABCMeta

    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        self.bot = bot
        self.dp = dp
        self.services = services
        self.wrap()

    async def file_download(self, file_id: str, extension: str) -> str:
        file = await self.bot.get_file(file_id)
        file_path = f'static/{file.file_unique_id}.{extension}'
        await self.bot.download_file(file.file_path, file_path)
        return file_path

    def wrap(self) -> None:
        pass
