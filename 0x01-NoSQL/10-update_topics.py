#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""


def insert_school(mongo_collection, **kwargs):
    """changes all topics of a school document based on the name"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
