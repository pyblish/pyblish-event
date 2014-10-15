
import sys
import json
import time

import flask
import flask.ext.restful
import flask.ext.socketio

app = flask.Flask(__name__)
app.debug = True

api = flask.ext.restful.Api(app)
socket = flask.ext.socketio.SocketIO(app)
thread = None

with open('static/data.json') as f:
    data = json.load(f)


class Api(flask.ext.restful.Resource):
    def get(self):
        return data

    def put(self):
        name = flask.request.form['name']
        new_data = {'name': name,
                    "type": "publish",
                    "source": sys.executable,
                    "date": time.ctime()}

        # Add to persistent datastore
        data.append(new_data)

        # Push to clients
        socket.emit("event",
                    new_data,
                    namespace="/test")


api.add_resource(Api, '/api')


@app.route("/")
def index():
    sorted_data = sorted(data, key=lambda k: k['date'])
    return flask.render_template('index.html', published=sorted_data)


@app.route('/event/<name>')
def details(name):
    names = dict((i['name'], i) for i in data)
    name = names.get(name)
    if name:
        return flask.render_template('publish-detail.html', publish=name)
    return ""


@socket.on("connect", namespace="/test")
def test_connect():
    flask.ext.socketio.emit("connected", {"data": "Connected", "count": 0})


if __name__ == "__main__":
    socket.run(app)
