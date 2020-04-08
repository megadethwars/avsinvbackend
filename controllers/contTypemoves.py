from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.datatypemoves import TypemovesDB
from status.status import Httpstatus
import traceback

@app.route('/typemoves')
def Getmoves():

    try:
        data = TypemovesDB.getmoves()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'



@app.route('/typemoves/<name>')
def GetMove(name):
    try:
        data = TypemovesDB.getMove(name)
        
        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'


@app.route('/posttypemove', methods = ['POST'])
def PostMove():
    try:
        
        if request.is_json:
            content = request.get_json()
            status = TypemovesDB.postMove(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except Exception as e:  
        print(e)      
        return Httpstatus.int_server('server error')




@app.route('/puttypemove/<id>',methods = ['PUT'])
def putMove(id):
    try:
        print(request.is_json)
        if request.is_json:

            content = request.json
            print(content)

            status=TypemovesDB.putMove(id,content)

            if status == 0:
                return Httpstatus.ok_server_put('ok')

            elif status == 1:

                return Httpstatus.not_found('not found')

            else:

                return Httpstatus.int_server('server error')

        else:
            return Httpstatus.bad_request('bad request')
        
    except:
        print('error')
        return Httpstatus.int_server('server error')