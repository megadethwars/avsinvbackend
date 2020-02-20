from flask import Flask
from test import MyClass


a=MyClass()

a.foo()


app = Flask(__name__)




import testroute
import testroute2


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/test")
def test():
    return "Hello test"


@app.route("/test2")
def test2():
    return "Hello test2"
    