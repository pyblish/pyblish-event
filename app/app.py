# Standard library
import os
import platform

# Dependencies
import flask
import flask.ext.socketio

# Local library
import routes.home


# App
app = flask.Flask(__name__)
app.route("/", defaults={"p": ""})(routes.home.route)
app.route("/<path:p>")(routes.home.route)


# Socket.io
socketio = flask.ext.socketio.SocketIO(app)


@socketio.on("connect", namespace="/default")
def connect():
    # Return hostname of computer running Flask upon connecting
    flask.ext.socketio.emit("connected", platform.node())


def debug(app):
    os.environ["DEVELOP"] = "true"
    app.debug = True
    # return app.run()
    return socketio.run(app)


def production(app):
    return socketio.run(app)


if __name__ == "__main__":
    debug(app)
