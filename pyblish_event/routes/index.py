import flask
from .. import app


@app.route('/', defaults={"p": ""})
@app.route('/<path:p>')
def root(p):
    with open("pyblish_event/static/index.html") as f:
        content = f.read()
    return flask.make_response(content)
