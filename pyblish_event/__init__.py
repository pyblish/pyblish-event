import flask
import flask.ext.socketio  # Runs gevent.monkey.patch_all()
import flask.ext.restful
import flask.ext.restful.reqparse

import pymongo
import datetime


def connect_to_database():
    client = pymongo.MongoClient()
    db = client.events_db
    events = db.events
    return events


def create_application(debug=True):
    app = flask.Flask(__name__)
    app.debug = debug

    socket = flask.ext.socketio.SocketIO(app)

    return app, socket

db = connect_to_database()
app, socket = create_application()
api = flask.ext.restful.Api(app)

parser = flask.ext.restful.reqparse.RequestParser()
parser.add_argument('event', type=str)


class ApiEvent(flask.ext.restful.Resource):
    def get(self):
        return list(db.find(fields={"_id": False}))

    def post(self):
        args = parser.parse_args()

        document = {"title": args['event'],
                    "content": datetime.datetime.utcnow().ctime()}

        # Add to persistent datastore
        document_id = db.insert(document.copy())

        # Push to clients
        socket.emit("event",
                    document,
                    namespace="/event")

        return str(document_id)


api.add_resource(ApiEvent, "/api")


# Subscribe to events

@socket.on("connect", namespace="/event")
def on_connect():
    """Initialise application with data from Database"""
    initial_data = list(db.find(fields={"_id": False}))

    data = {
        "whois": "pyblish_event",
        "events": initial_data
    }

    print "Sending initial data: %s" % data
    flask.ext.socketio.emit("connected", data)


from .routes import index
