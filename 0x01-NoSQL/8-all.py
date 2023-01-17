#!/usr/bin/env python3
"""Module: 8-all"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    count = mongo_collection.count_documents({})
    if count == 0:
        return []
    return mongo_collection.find()
