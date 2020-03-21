from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataInvent import InventDB
from status.status import Httpstatus



@app.route('/devices')
def GetDevices():

    try:
        data = InventDB.getDevices()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    

  

@app.route('/devicecode/<name>')
def GetDevice(name):
    try:
        data = InventDB.getDevicesbycode(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    


@app.route('/devicename')
def GetDevicebyname():
    try:

        name = request.args.get('nombre')
        data = InventDB.getDevicesbyname(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')  



@app.route('/postDevice', methods = ['POST'])
def PostDevice():

    try:
        print(request.is_json)
        if request.is_json:
            content = request.get_json()
            
            

            status = InventDB.postDevice(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')




    #print (request.is_json)
    #content = request.get_json()
    
    #if request.is_json:
    #    status = UserDB.postUser(content)

    ##starting to create user to sql
    #return 'OK', 201




@app.route('/putdevice/<string:name>',methods = ['PUT'])
def PutDevice(name):
    
    try:

        if request.is_json:

            content = request.json

            status=InventDB.putDevice(content,name)

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
        return int_server('server error')

   

@app.route('/deldevice/<string:name>',methods = ['DELETE'])
def deldevice(name):
    try:
          
        status=InventDB.delDevice(name)

        if status == 0:
            return Httpstatus.ok_server_put('ok')

        elif status == 1:

            return Httpstatus.not_found('not found')

        else:

            return Httpstatus.int_server('server error')
  
    except:
        return Httpstatus.int_server('server error')
        


