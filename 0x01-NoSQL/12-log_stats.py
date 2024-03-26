#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""
from pymongo import MongoClient



if __name__ == "__main__":
    """provides stats about nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx
    print("{} logs".format(coll.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = coll.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, count))

    status_get = coll.count_documents({'method': 'GET', 'path': "/status"})
    print("{} status check".format(status_get))
    