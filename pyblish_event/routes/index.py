import os
import flask
from .. import app

index = "pyblish_event/static/index.html"


def response_develop():
    """During development, do not cache"""
    with open(index) as f:
        content = f.read()
    return flask.make_response(content)


def response_production():
    """During production, cache for improved performance"""
    return flask.send_file(index)


@app.route('/', defaults={"p": ""})
@app.route('/<path:p>')
def root(p):
    """Route all paths to the same address and let Angular do its thing"""
    if os.environ.get('DEVELOP', "false") == "true":
        return response_develop()
    return response_production()
