from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.datahistorial import HistorialDB
from status.status import Httpstatus
import datetime

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


@app.route('/movesearch')
def GetMovementsbysearch():

    try:
        #["movimiento","lugar","usuario","producto","fecha","modelo","marca","codigo","serie"]
        
        lista=[]
        
        
        try:
            lista.append(request.args.get('IDmovimiento'))
            lista.append(request.args.get('IDtipomov'))      
            lista.append(request.args.get('IDlugar'))
            lista.append(request.args.get('IDusuario'))
            lista.append(request.args.get('producto'))
            lista.append(request.args.get('fechamovimiento'))
            lista.append(request.args.get('modelo'))
            lista.append(request.args.get('marca'))
            lista.append(request.args.get('codigo'))
            lista.append(request.args.get('serie'))
            
            if request.args.get('fechamovimiento')!="null":
                datetime.datetime.strptime(request.args.get('fechamovimiento'),"%Y-%m-%d").date()

        except Exception as e:
            print(e)
            return Httpstatus.bad_request('bad_request')
            
        
        #movimiento = request.args.get('movimiento')
        if len(lista) !=10:
            return Httpstatus.bad_request('bad request')
        data = HistorialDB.getHistorialbysearch(lista)
        

        

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except Exception as e:
        print(e)
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