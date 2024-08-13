#!/usr/bin/env python3
"""insert school"""


def insert_school(mongo_collection, **kwargs):
    """
    insert an item to our collection and return the ID
    """
    return mongo_collection.insert_one(kwargs).inserted_id
