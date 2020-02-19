from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello Flask"


@myapp.route("/test")
def test():
    return "Hello test"
