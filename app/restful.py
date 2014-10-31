import json
import uuid
import time

import flask.ext.restful

import model


def api(socket):
    class Api(flask.ext.restful.Resource):
        def get(self):
            return model.data

        def post(self):
            unique_id = str(uuid.uuid4())

            event_str = flask.request.stream.read()
            event = json.loads(event_str)
            event["id"] = unique_id

            if not "date" in event:
                event["date"] = time.time()

            if not "family" in event:
                event["family"] = "nofamily"

            socket.emit("event",
                        event,
                        namespace="/default")

            model.add_event(event)

            return unique_id

    return Api
