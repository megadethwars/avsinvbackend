from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataInvent import InventDB
from status.status import Httpstatus
import datetime


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


@app.route('/deviceid/<name>')
def GetDeviceid(name):
    try:
        data = InventDB.getDevicesbyID(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')



@app.route('/devicemarca/<name>')
def GetDevicemarca(name):
    try:
        data = InventDB.getDevicesbymarca(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')

    
@app.route('/devicemodelo/<name>')
def GetDevicemodelo(name):
    try:
        data = InventDB.getDevicesbymodelo(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')


@app.route('/deviceserie')
def GetDeviceserie():
    try:

        name = request.args.get('serie')
        data = InventDB.getDevicesbyserie(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')


@app.route('/deviceprov/<name>')
def GetDeviceprov(name):
    try:
        data = InventDB.getDevicesbyproveedor(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')



@app.route('/devicesearch')
def Getdevicesbysearch():

    try:
        #["codigo","producto","fecha","modelo","marca","serie"]
        
        lista=[]
        
        
        try:
            lista.append(request.args.get('codigo'))
            lista.append(request.args.get('producto'))
            lista.append(request.args.get('fecha'))
            lista.append(request.args.get('modelo'))           
            lista.append(request.args.get('marca'))
            lista.append(request.args.get('serie'))
            
            
            if request.args.get('fecha')!="null":
                datetime.datetime.strptime(request.args.get('fecha'),"%Y-%m-%d").date()

        except Exception as e:
            print(e)
            return Httpstatus.bad_request('bad_request')
            
        
        #movimiento = request.args.get('movimiento')
        if len(lista) !=6:
            return Httpstatus.bad_request('bad request')
        data = InventDB.getDevicesbysearch(lista)
        

        

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except Exception as e:
        print(e)
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
            elif status==2:
                return Httpstatus.int_server('server error')
            elif status == 1:
                return Httpstatus.conflict('ya existente')

            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')





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

      
@app.route('/deldevice/<string:id>',methods = ['DELETE'])
def deldevice(id):
    try:
          
        status=InventDB.delDevice(id)

        if status == 0:
            return Httpstatus.ok_server_put('ok')

        elif status == 1:

            return Httpstatus.not_found('not found')

        elif status == 2:

            return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.conflict('Conflicto al borrar')
  
    except:
        return Httpstatus.int_server('server error')



@app.route('/validatesamedevices', methods = ['POST'])
def ValidateSame():

    try:
        print(request.is_json)
        if request.is_json:
            content = request.get_json()
            
            status = InventDB.ValidateSamePlaces(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            elif status==2:
                return Httpstatus.conflict('not the same')
            elif status == 1:
                return Httpstatus.not_found('not found')

            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')



@app.route('/missingdevices/<name>')
def SearchMissing(name):
    try:
        data = InventDB.getDevicesMissing(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')