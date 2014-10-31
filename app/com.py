import platform
import flask.ext.socketio


def connect():
    # Return hostname of computer running Flask upon connecting
    flask.ext.socketio.emit("connected", platform.node())
