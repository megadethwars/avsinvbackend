from flask import Flask,Response,abort
import pyodbc
from test import MyClass
from data.Service import ServiceSQL 



#a=MyClass()

#a.foo()

ServiceSQL.InitConexion()
app = Flask(__name__)




import testroute
import testroute2
from controllers import contuser


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/test")
def test():
    return "Hello test"


@app.route("/test2")
def test2():
    return "Hello test2"
    