from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('from server',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()

    return render_template('index.html')


@socketio.on('echo', namespace='/test')
def test_message(message):
    session['receive_count'] += 1
    emit('from server',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('broadcast', namespace='/test')
def test_message(message):
    session['receive_count'] += 1
    emit('from server',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('connected', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
