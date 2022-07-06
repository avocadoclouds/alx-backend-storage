#!/usr/bin/env python3

"""
a Python function that changes all topics of a school document based on the name:
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
     changes all topics of a school document based on the name
     name (str): school name to update
     topics (list of str): list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
