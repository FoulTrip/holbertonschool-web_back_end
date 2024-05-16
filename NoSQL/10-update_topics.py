#!/usr/bin/env python3
""" changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """Change school topics"""
    filter = {"name": name}
    update = {"$set": {"topics": topics}}
    put_topics = mongo_collection.update_many(filter, update)
