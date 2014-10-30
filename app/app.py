import os
import flask
import routes.home


app = flask.Flask(__name__)
app.route("/", defaults={"p": ""})(routes.home.route)
app.route("/<path:p>")(routes.home.route)


if __name__ == "__main__":
    os.environ["DEVELOP"] = "true"
    app.run(debug=True)
