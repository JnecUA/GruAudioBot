from aiogram import Bot, Dispatcher
from handlers.start_handler import StartHandler
from handlers.profile.profile_handler import ProfileHandler
from services.service import Services


class MainHandler:
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        handlers = [StartHandler, ProfileHandler]
        for handler in handlers:
            handler(bot, dp, services)
