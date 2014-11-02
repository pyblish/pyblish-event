
# Dependencies
import flask
import flask.ext.restful
import flask.ext.socketio

# Local library
import com
import rest
import routes.home


# App
app = flask.Flask(__name__)
app.route("/", defaults={"p": ""})(routes.home.route)
app.route("/<path:p>")(routes.home.route)  # All paths route to index.html


# Socket.io
socket = flask.ext.socketio.SocketIO(app)
socket.on("connect", namespace="/default")(com.connect)


# RESTful
api = flask.ext.restful.Api(app)
api.add_resource(type("Api", (rest.api(socket=socket),), {}), "/api")
api.add_resource(type("Event", (rest.api(socket=socket),), {}), "/event")


def debug(app):
    app.debug = True
    return socket.run(app)


def production(app):
    return socket.run(app)


if __name__ == "__main__":
    debug(app)
