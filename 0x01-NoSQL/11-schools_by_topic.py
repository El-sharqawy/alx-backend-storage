#!/usr/bin/env python3
"""schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """
    returns a list of schools that having a specific topic
    """
    return mongo_collection.find({"topics": topic})
