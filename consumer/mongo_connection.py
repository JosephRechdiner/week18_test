from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

class MongoManager():
    client = None
    def __init__(self):
        try:
            if not MongoManager.client:
                MongoManager.client = MongoClient(MONGO_URI)
            self.client = MongoManager.client
        except Exception as e:
            raise Exception(f"Could not connect to MongoDB, Error: {str(e)}")
        
    def get_client(self):
        return self.client