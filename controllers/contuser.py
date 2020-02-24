from run import app
from data.Service import ServiceSQL
from data.dataUser import UserDB

#get users

def bad_request(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response

def int_server(message):
    response = jsonify({'message': message})
    response.status_code = 500
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
        return 'bad request!', 500
    

    return 'postuser'









