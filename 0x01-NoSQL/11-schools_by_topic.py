#!/usr/bin/env python3
"""
function that changes all topics of a school documnent based on
the name
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
