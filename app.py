import flask

HOSTNAME="aaryab.in"
app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def GET_index():
    if "X-Forwarded-Host" in flask.request.headers:
        host = flask.request.headers["X-Forwarded-Host"]
        if "test." + HOSTNAME in host:
            return host, 200

    return flask.render_template("index.html", params={ "title": "Aarya Bhatia" })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

