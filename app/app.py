# Standard library
import os

# Dependencies
import flask
import flask.ext.restful
import flask.ext.socketio

# Local library
import com
import routes.home


# App
app = flask.Flask(__name__)
app.route("/", defaults={"p": ""})(routes.home.route)
app.route("/<path:p>")(routes.home.route)  # All paths route to index.html


# Socket.io
socketio = flask.ext.socketio.SocketIO(app)
socketio.on("connect", namespace="/default")(com.connect)


# RESTful API
api = flask.ext.restful.Api(app)


def debug(app):
    os.environ["DEVELOP"] = "true"
    app.debug = True
    return socketio.run(app)


def production(app):
    return socketio.run(app)


if __name__ == "__main__":
    debug(app)
