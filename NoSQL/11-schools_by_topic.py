#!/usr/bin/env python3
""" list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """returns a list with a specific topic"""
    topic_search = mongo_collection.find({"topics": topic})
    return topic_search
