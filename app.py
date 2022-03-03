import flask
app = flask.Flask(__name__)

@app.route("/test", methods=['GET'])
def index():
    return "Hello Heruko"