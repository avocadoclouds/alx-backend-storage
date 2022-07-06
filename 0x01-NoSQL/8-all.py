#!/usr/bin/env python3

"""
a Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """
    lists all documnets in a collection
    returns an empty lust if document in collection
    """
    return [each for each in mongo_collection.find()]


"""
return [each for each in mongo_collection.find()]
and
return  mongo_collection.find()
have the same result
"""
