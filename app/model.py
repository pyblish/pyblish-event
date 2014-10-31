import pymongo

try:
    client = pymongo.MongoClient()
except:
    # This will get output in the terminal is a user
    # should try and launch without having installed Mongo
    raise ValueError("MongoDB must be installed")

db = client.pyblish_database
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


# data = []

# for i in xrange(30):
#     data.append({
#         "instance": [
#             "Peter01",
#             "Marus02",
#             "RobotVillain05",
#             "TestBot10"
#         ][random.randint(0, 3)],
#         "color": random.randint(0, 4),
#         "comment": "Some long comment here",
#         "author": "marcus",
#         "date": time.time(),
#         "family": [
#             "napoleon.animation.rig",
#             "napoleon.asset.rig",
#             "napoleon.animation.cache",
#             "napoleon.asset.model",
#             "napoleon.asset.texture",
#             "napoleon.asset.shd",
#             "napoleon.asset.shader",
#             "napoleon.asset.panzar",
#             "napoleon.asset.moosh",
#             "napoleon.animation.blood",
#             "napoleon.asset.mod",
#             "napoleon.asset.abc",
#             "napoleon.asset.dawn",
#             "napoleon.asset.texture",
#         ][random.randint(0, 13)]
#     })
