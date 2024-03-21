# repositories.py

import pymongo
from django.conf import settings

# repositories.py

class WeatherRepository:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        collection = self.getCollection()
        documents = collection.find({})
        return documents
    
    def insert(self, document):
        collection = self.getCollection()
        collection.insert_one(document)