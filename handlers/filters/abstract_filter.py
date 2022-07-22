from aiogram.dispatcher.filters import Filter
from db import Database
from services.service import Services

services = Services(Database())


class AbstractFilter(Filter):
    def __init__(self) -> None:
        self.services = services

    def check():
        pass
