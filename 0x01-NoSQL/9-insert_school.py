#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new documents in a collection and returns the id"""
    myid = mongo_collection.insert_one(kwargs)
    return myid.inserted_id
