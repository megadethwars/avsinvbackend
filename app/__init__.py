from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/test")
def test():
    return "Hello test"


@app.route("/test2")
def test2():
    return "Hello test2"