from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.datahistorial import HistorialDB
from status.status import Httpstatus


@app.route('/moves')
def GetMovements():

    try:
        
        data = HistorialDB.getHistorial()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')


@app.route('/postmove', methods = ['POST'])
def PostHistorial():

    try:
        print(request.is_json)
        if request.is_json:
            content = request.get_json()
            
            
            status = HistorialDB.postHistorial(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')