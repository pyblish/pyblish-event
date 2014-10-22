import flask
import flask.ext.socketio

app = flask.Flask(__name__)
app.debug = True

socket = flask.ext.socketio.SocketIO(app)


events = [
    {"title": "Peter01",
     "content": "Peter01 was published just now"},
    {"title": "Marcus04",
     "content": "Marcus04 was published 6 mins ago"}]


@socket.on("connect", namespace="/event")
def on_connect():
    data = {"whois": "pyblish_event",
            "events": events}
    flask.ext.socketio.emit("connected", data)


from .routes import index
