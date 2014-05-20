__author__ = 'mudit'
from pymongo import MongoClient
import datetime

class adapter():

    def push(self, collection_name):
        client = MongoClient()
        db = client.sfdc_database
        name = collection_name
        collection = db[name]

