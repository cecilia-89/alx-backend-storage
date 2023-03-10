#!/usr/bin/env python3
"""Module: 11-schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    query = mongo_collection.find({"topics": topic})
    return query
