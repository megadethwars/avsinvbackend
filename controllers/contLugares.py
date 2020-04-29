from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataLugares import LugarDB
from status.status import Httpstatus
import traceback

@app.route('/lugares')
def GetLugares():

    try:
        data = LugarDB.getLugares()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'



@app.route('/lugares/<name>')
def GetLugar(name):
    try:
        data = LugarDB.getLugar(name)
        
        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'


@app.route('/postlugar', methods = ['POST'])
def PostLugar():
    try:
        
        if request.is_json:
            content = request.get_json()
            status = LugarDB.postLugar(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            elif status == 2:
                return Httpstatus.int_server('server error')
            elif status == 1:
                return Httpstatus.conflict('Conflicto')
        
        else:
            return Httpstatus.bad_request('bad request')

    except Exception as e:
        print(e)        
        return Httpstatus.int_server('server error')




@app.route('/putlugar/<id>',methods = ['PUT'])
def putLugar(id):
    try:
        print(request.is_json)
        if request.is_json:
       
            content = request.json
            

            status=LugarDB.putLugar(id,content)

            if status == 0:
                return Httpstatus.ok_server_put('ok')

            elif status == 1:

                return Httpstatus.not_found('not found')

            else:

                return Httpstatus.int_server('server error')

        else:
            return Httpstatus.bad_request('bad request')
        
    except Exception as e:
        print(e)
        return Httpstatus.int_server('server error')