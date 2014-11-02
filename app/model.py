import os
import pymongo

MONGO_URL = os.environ.get('MONGOHQ_URL')

try:
    client = pymongo.MongoClient(MONGO_URL)
except:
    # This will get output in the terminal is a user
    # should try and launch without having installed Mongo
    raise ValueError("MongoDB must be installed")

db = getattr(client, "app31128273")
events = db.events
excludes = {"_id": False}


def all_events():
    """Return all available events"""
    return list(events.find(fields=excludes))


def add_event(event):
    """Add a single event

    Arguments:
        event (dict): A single event as dictionary

    """

    events.insert(event)


def remove_event(event):
    raise NotImplementedError
