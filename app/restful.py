import json
import flask.ext.restful
import uuid

import model


def api(socket):
    class Api(flask.ext.restful.Resource):
        def get(self):
            return model.data

        def post(self):
            unique_id = str(uuid.uuid4())

            event = flask.request.stream.read()
            event_json = json.loads(event)
            event_json['id'] = unique_id

            # model.data.append(event_json)

            print "Emitting %s" % event_json
            socket.emit("event",
                        event_json,
                        namespace="/default")

            return unique_id

    return Api
