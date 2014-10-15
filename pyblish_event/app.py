import os
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

package_dir = os.path.dirname(__file__)
data_path = os.path.join(package_dir, 'static', 'data.json')
with open(data_path) as f:
    data = json.load(f)


class Api(flask.ext.restful.Resource):
    def get(self):
        """Return all current events"""
        return [k['name'] for k in data]

    def put(self):
        """Add new event"""
        name = flask.request.form['name']
        new_data = {'name': name,
                    "type": "publish",
                    "source": sys.executable,
                    "date": time.ctime()}

        # Persist data, in-memory and on-disk
        data.append(new_data)
        with open(data_path, 'w') as f:
            json.dump(data, f, indent=4)

        # Push to clients
        socket.emit("event",
                    new_data,
                    namespace="/test")


api.add_resource(Api, '/api')


@app.route("/")
def index():
    sorted_data = sorted(data, key=lambda k: k['date'], reverse=True)
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
