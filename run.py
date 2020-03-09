from flask import Flask,Response,abort,request

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
from controllers import continvent
from controllers import contreport

@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/test")
def test():
    return "Hello test"


@app.route("/test2")
def test2():
    return "Hello test2"
    