import logging

from aiogram import Bot, Dispatcher, executor

from handlers.main_handler import MainHandler

class GruBot:
    def __init__(self, token) -> None:
        self.bot = Bot(token)
        logging.basicConfig(level=logging.INFO)
        self.dp = Dispatcher(self.bot)
        MainHandler(self.dp)        

    def start(self) -> None:
        executor.start_polling(self.dp, skip_updates=True)