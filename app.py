import flask

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def GET_index():
    print(flask.request.headers)
    return flask.render_template("index.html", params={ "title": "Aarya Bhatia" })

@app.route("/<path>")
def all_routes(path):
    print(path)
    return "", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
