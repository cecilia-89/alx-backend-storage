#!/usr/bin/env python3
"""Module: 9-insert"""


if __name__ == '__main__':
    def insert_school(mongo_collection, **kwargs):
        """inserts a new document in a collection"""
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
