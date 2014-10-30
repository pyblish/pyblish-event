import os
import flask

index = "static/index.html"


def _response_develop():
    """During development, do not cache"""
    print "Running development server"
    with open(index) as f:
        content = f.read()
    return flask.make_response(content)


def _response_production():
    """During production, cache for improved performance"""
    print "Running production server"
    return flask.send_file(index)


def route(p):
    """Route all paths to the same address and let Angular do its thing"""
    if os.environ.get("DEVELOP", "false") == "true":
        return _response_develop()
    return _response_production()
