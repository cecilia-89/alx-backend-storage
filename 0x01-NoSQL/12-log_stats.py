#!/usr/bin/env python3
from pymongo import MongoClient

if __name__ == "__main__":
    db = MongoClient().logs
    collection = db.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("{} logs\nMethods:".format(collection.count_documents({})))
    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            len(list(collection.find({"method": method})))
        ))

    print("{} status check".format(len(list(collection.aggregate([
        {"$match": {"method": "GET"}},
        {"$match": {"path": "/status"}}]
        )))))
