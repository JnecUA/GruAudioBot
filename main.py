from bot import GruBot
import configs

from db import Database
from services.service import Services

config = configs.load('.conf') 
db = Database(uri=config["db"]["uri"])
services = Services(db)
bot = GruBot(token=config["bot"]["api_token"], services=services)
bot.start()