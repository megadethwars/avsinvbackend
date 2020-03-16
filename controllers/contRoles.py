from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataRoles import RoleDB
from status.status import Httpstatus

@app.route('/roles')
def GetRoles():

    try:
        data = RoleDB.getRoles()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'



@app.route('/roles/<name>')
def GetRole(name):
    try:
        data = RoleDB.getRole(name)
        
        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    
    return 'postuser'


@app.route('/postRole', methods = ['POST'])
def PostRole():
    try:
        
        if request.is_json:
            content = request.get_json()
            status = RoleDB.postRole(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')




@app.route('/putrole/<id>',methods = ['PUT'])
def putRole(id):
    try:
        print(request.is_json)
        if request.is_json:

            content = request.json
            print(content)

            status=RoleDB.putRole(id,content)

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