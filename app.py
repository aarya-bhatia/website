import flask
import requests

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def GET_index():
    return flask.render_template("index.html")
