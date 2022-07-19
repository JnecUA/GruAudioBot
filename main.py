from bot import GruBot
import configs

conf = configs.load('.conf')
bot = GruBot(token=conf["bot"]["api_token"])
bot.start()