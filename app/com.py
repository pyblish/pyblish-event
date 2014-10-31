import platform
import flask.ext.socketio

import model


def connect():
    """Return hostname of computer running Flask upon connecting"""
    flask.ext.socketio.emit("connected", platform.node())
    flask.ext.socketio.emit("init", {"events": model.data})
