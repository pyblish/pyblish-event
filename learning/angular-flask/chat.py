import gevent.monkey
gevent.monkey.patch_all()

import time
import threading

import flask
import flask.ext.triangle
import flask.ext.socketio

app = flask.Flask(__name__)
app.debug = True

# Apply triangle
flask.ext.triangle.Triangle(app)

# Apply socketio
socket = flask.ext.socketio.SocketIO(app)

thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(2)
        count += 1
        socket.emit('background',
                    'ricardo')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = threading.Thread(target=background_thread)
        thread.daemon = True
        thread.start()

    return flask.render_template('index.html')


@socket.on("first name to server")
def listen(value):
    print "Emitting: %s" % value
    flask.ext.socketio.emit("to client", value[::-1])


@socket.on("connect")
def test_connect():
    flask.ext.socketio.emit("connected", {"data": "Connected", "count": 0})


@socket.on("disconnect")
def test_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socket.run(app)
