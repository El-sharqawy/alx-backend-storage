#!/usr/bin/env python3
"""Top Students"""


def top_students(mongo_collection):
    """
    returns all the students sorted ASC by average score
    """
    return mongo_collection.aggregate(
        [
            {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
