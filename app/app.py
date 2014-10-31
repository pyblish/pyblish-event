# Standard library
import os
import time
import threading

# Dependencies
import flask
import flask.ext.restful
import flask.ext.socketio

# Local library
import com
# import restful
import routes.home


# App
app = flask.Flask(__name__)
app.route("/", defaults={"p": ""})(routes.home.route)
app.route("/<path:p>")(routes.home.route)  # All paths route to index.html


# Socket.io
_socketio = flask.ext.socketio.SocketIO(app)
_socketio.on("connect", namespace="/default")(com.connect)


# RESTful API
# _api = flask.ext.restful.Api(app)
# _api.add_resource(restful.api(socket=_socketio, data={}), "/api")


def background_push():
    while True:
        print "Pushing.."
        time.sleep(2)
        _socketio.emit("event", {
            "instance": "From Flask",
            "family": "napoleon.test",
            "comment": "Flask comment",
            "author": "Maaaarcus"},
            namespace="/default")


print "Starting thread.."
thread = threading.Thread(target=background_push)
thread.daemon = True
thread.start()


def debug(app):
    os.environ["DEVELOP"] = "true"
    app.debug = True
    return _socketio.run(app)


def production(app):
    return _socketio.run(app)


if __name__ == "__main__":
    debug(app)
