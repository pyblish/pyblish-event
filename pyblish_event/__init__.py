import flask

app = flask.Flask(__name__)


from .routes import index
