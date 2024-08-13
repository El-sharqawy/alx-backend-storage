#!/usr/bin/env python3
"""list all"""


def list_all(mongo_collection):
    """
    get all docs in our mongo collection
    """

    return mongo_collection.find()
