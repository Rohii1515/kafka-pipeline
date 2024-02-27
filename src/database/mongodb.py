import pymongo  # This module provides tools to work with MongoDB databases in Python.
import os  # This module interacts with the operating system.
import certifi  # This module helps with certificates used for secure connections (TLS/SSL).

ca = certifi.where()
    # Finds the location of the certificate authority (CA) file used for verifying secure connections (TLS/SSL). 
    # It's important to establish a secure connection when working with sensitive data like database interactions.

class MongodbOperation:
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"), tlsCAFile=ca)
        self.db_name = "sensor_Data"

    def insert_many(self, collection_name, records: list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self, collection_name, record):
        self.client[self.db_name][collection_name].insert_one(record)
