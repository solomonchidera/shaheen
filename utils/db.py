"""a utility module to handle mongo db database
"""
from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
load_dotenv()
URI = getenv('DB_CONNECTION_STRING')


class DB:
    def __init__(self, collection_name):
        self.client = MongoClient(URI)
        self.database = self.client['shaheen']
        self.collection = self.database[collection_name]

    def insert_one(self, document):
        """Insert a single document into the collection."""
        result = self.collection.insert_one(document)
        return result.inserted_id

    def insert_many(self, documents):
        """Insert multiple documents into the collection."""
        result = self.collection.insert_many(documents)
        return result.inserted_ids

    def find_one(self, query):
        """Find a single document based on the query."""
        return self.collection.find_one(query)

    def close(self):
        """Close the connection to the database."""
        self.client.close()
