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


@app.route('/movesearch')
def GetMovementsbysearch():

    try:
        #["movimiento","lugar","usuario","producto","fecha","modelo","marca","codigo","serie"]
        
        lista=[]
        
        
        try:
            lista.append(request.args.get('movimiento'))
            lista.append(request.args.get('lugar'))
            lista.append(request.args.get('usuario'))
            lista.append(request.args.get('producto'))
            lista.append(request.args.get('fecha'))
            lista.append(request.args.get('modelo'))
            lista.append(request.args.get('marca'))
            lista.append(request.args.get('codigo'))
            lista.append(request.args.get('serie'))

        except:
            return Httpstatus.bad_request('bad_request')
            
        print(len(lista))
        #movimiento = request.args.get('movimiento')
        if len(lista) !=9:
            return Httpstatus.bad_request('bad request')
        data = HistorialDB.getHistorialbysearch(lista)
        

        

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