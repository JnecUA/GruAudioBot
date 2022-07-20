import logging

from aiogram import Bot, Dispatcher, executor
from db import Database

from handlers.main_handler import MainHandler
from services.service import Services

class GruBot:
    def __init__(self, token: str, services: Services) -> None:
        self.bot = Bot(token)
        logging.basicConfig(level=logging.INFO)
        self.dp = Dispatcher(self.bot)
        MainHandler(self.dp, services)        

    def start(self) -> None:
        executor.start_polling(self.dp, skip_updates=True)