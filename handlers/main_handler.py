from aiogram import Bot, Dispatcher
from handlers.start_handler import StartHandler
from services.service import Services


class MainHandler:
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        StartHandler(bot, dp, services)
