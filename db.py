from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection

class Database:
    def __init__(self, uri) -> None:
        self.uri = uri
        client = MongoClient(self.uri)
        self.db = client.get_database("GruAudioBot")

    def get_collection(self, collection_name: str) -> Collection:
        return self.db[collection_name]