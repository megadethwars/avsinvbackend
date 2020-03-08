from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataUser import UserDB


#get users

def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'message': message})
    response.status_code = 404
    return response

def int_server(message):
    response = jsonify({'message': message})
    response.status_code = 500
    return response

def ok_server_post(message='ok'):
    response = jsonify({'message': message})
    response.status_code = 201
    return response


def ok_server_put(message='ok'):
    response = jsonify({'message': message})
    response.status_code = 200
    return response

@app.route('/users')
def GetUsers():

    try:
        data = UserDB.executePost()

        if data == None:
            int_server('message that appears in body')
        elif data == []:
            bad_request('message that appears in body')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return 'internal server error!', 500
    

    return 'postuser'

@app.route('/user/<name>')
def GetUser(name):
    try:
        data = UserDB.GetUser(name)

        if data == 1:
            return not_found('not found')


        if data == None:
            return int_server('message that appears in body')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return int_server('server error')
    

    return 'postuser'

@app.route('/postUser', methods = ['POST'])
def Postuser():

    try:
        
        if request.is_json:
            content = request.get_json()
            status = UserDB.postUser(content)

            if status == 0:
                return ok_server_post()
            else:
                return int_server('server error')

    except:        
        return int_server('server error')




    #print (request.is_json)
    #content = request.get_json()
    
    #if request.is_json:
    #    status = UserDB.postUser(content)

    ##starting to create user to sql
    #return 'OK', 201




@app.route('/putuser/<string:name>',methods = ['PUT'])
def Putuser(name):
    print("testing")
    try:

        if request.is_json:

            content = request.json

            status=UserDB.putUser(content)

            if status == 0:
                return ok_server_put('ok')

            elif status == 1:

                return not_found('not found')

            else:

                return int_server('server error')

        else:
            return bad_request('bad request')
        
    except:
        return int_server('server error')

   
