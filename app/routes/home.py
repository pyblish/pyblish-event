import flask

index = "static/index.html"


def route(p):
    """Route all paths to the same address and let Angular do its thing"""
    return flask.send_file(index)
