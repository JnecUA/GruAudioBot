from aiogram import Dispatcher
from db import Database
from handlers.start_handler import StartHandler
from services.service import Services

class MainHandler:
    def __init__(self, dp: Dispatcher, services: Services) -> None:
        StartHandler(dp, services)