import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
import configs


class Database:
    def __init__(self) -> None:
        config = configs.load('.conf')
        self.uri = config["db"]["uri"]
        client = AsyncIOMotorClient(self.uri, tlsCAFile=certifi.where())
        self.db = client.get_database("GruAudioBot")

    def get_collection(self, collection_name: str) -> Collection:
        return self.db[collection_name]
