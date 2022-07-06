#!/usr/bin/env python3

"""
a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    topic (string): the topic searched
    return a lsit of school
    """

    return mongo_collection.find({"topics": topic})
