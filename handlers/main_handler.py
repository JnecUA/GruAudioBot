from aiogram import Bot, Dispatcher
from handlers.memes.create_meme_handler import CreateMemeHandler
from handlers.memes.select_stretch_handler import SelectStretchHandler
from handlers.memes.wide_putin_handler import WidePutinHandler
from handlers.payments_handler import PaymentsHandler
from handlers.separate.select_separate_handler import SelectSeparateHandler
from handlers.separate.separate_handler import SeparateHandler
from handlers.start_handler import StartHandler
from handlers.menu_handler import MenuHandler
from services.service import Services


class MainHandler:
    def __init__(self, bot: Bot, dp: Dispatcher, services: Services) -> None:
        handlers = [StartHandler, MenuHandler,
                    CreateMemeHandler, WidePutinHandler, SelectStretchHandler, SeparateHandler, SelectSeparateHandler, PaymentsHandler]
        for handler in handlers:
            handler(bot, dp, services)
