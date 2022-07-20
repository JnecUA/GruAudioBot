from abc import ABCMeta

from aiogram import Dispatcher
from services.service import Services

class AbstractHandler:
    __metaclass__ = ABCMeta
    
    def __init__(self, dp: Dispatcher, services: Services) -> None:
        self.dp = dp
        self.services = services
        self.wrap()

    def wrap(self) -> None:
        pass