#!/usr/bin/env python3
"""
Module that lists all documents in a collection
Returns an empty list if no doc in the collection
"""


def list_all(mongo_collection):
    """Lists all docs"""
    documents = mongo_collection.find()
    return documents
