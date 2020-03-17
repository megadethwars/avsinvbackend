from flask import Flask,Response,abort,request

import pyodbc
from test import MyClass
from data.Service import ServiceSQL 
import threading


#a=MyClass()

#a.foo()

ServiceSQL.InitConexion()
health = threading.Thread(target=ServiceSQL.reconnect,daemon=True)
health.start()

app = Flask(__name__)




import testroute
import testroute2
from controllers import contuser
from controllers import continvent
from controllers import contreport
from controllers import conthistorial
from controllers import contRoles
from controllers import contLugares

@app.route("/")
def hello():
    status = ServiceSQL.reconncetOnce()

    if status==True:
        return "SQL Connected"
    else:

        return "SQL Disconnected"


@app.route("/test")
def test():
    return "Hello test"


@app.route("/test2")
def test2():
    return "Hello test2"
    