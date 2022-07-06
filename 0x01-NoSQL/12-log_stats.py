#!/usr/bin/env python3


"""
a Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the
method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it is a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""

from pymongo import MongoClient


def log_stats(nginx_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """

    # Fist line
    totalLogs = nginx_collection.count_documents({})
    print("{} logs".format(totalLogs))

    # Second line
    print('Methods:')

    # The 5 lines
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # tabulation \t
        print('\tmethod {}: {}'.format(method, count))

    # The final line (status check)
    status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
