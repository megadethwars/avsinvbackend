from data.Service import ServiceSQL
import json
from data.Service import ServiceSQL 
import traceback
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash

def strinsert(table,cols,obj):

    table = str(table)
    insertcmd = "insert into  " + table + " ("
    print(insertcmd)
    cont = 0

    for column in cols:
        insertcmd+="" + column + ","
        cont=cont+1
    insertcmd=insertcmd[0:-1]
    insertcmd+=") values ("

    cont2=0
    for value in obj.values():

        if type(value) is int:
            
            insertcmd+= str(value)+","
        else:
            insertcmd+="'" + value + "',"

        
        cont2=cont2+1

    insertcmd=insertcmd[0:-1]
    insertcmd+=")"    

    #print(insertcmd)
    return insertcmd


def strselect(table,argumentos,cols):
    select = ""

    select = str(select)

    select = "select * from "+table+" where "

    isfirst=False
    count = 0


    for column in argumentos:

        
        if column != "" and column != 'null':
            
            if isfirst==True:
                select+=" and " + cols[count] + " = '" + column + "' " 
            else:   
                select+="" + cols[count] + " = '" + column + "' " 

            isfirst = True
        
        count=count + 1

    #print(select)
    return select



def cmdinsert(table,objeto):
    table = str(table)
    TABLE_NAME = table

    sqlstatement = ''

    keylist = "("
    valuelist = "("
    firstPair = True
    for key, value in objeto.items():
        if key !='ID' and key !='fecha' and key!='tipousuario' and key!='rol' and key!='statuscode' and key!='message':
            if not firstPair:
                keylist += ", "
                valuelist += ", "
            firstPair = False
            keylist += key
            if type(value) is str:
                valuelist += "'" + value + "'"
            else:
                valuelist += str(value)
    keylist += ")"
    valuelist += ")"

    sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist
    #print(sqlstatement)
    return sqlstatement


def cmdupdate(table,objeto,name):
    table = str(table)
    TABLE_NAME = table

    sqlstatement = ''

    
    valuelist = ""
    firstPair = True
    for key, value in objeto.items():
        print(key,value)
        if key =='ID' or key =='fecha' or key=='tipousuario' or key=='rol' or key=='password' and key!='statuscode' and key!='message':
            a=1
        else:
            if type(value) is int:
                valuelist+=key + " = "+ str(value) + ","
            else:
                valuelist+=key + " = "+ "'" + value + "'" + ","
    
    valuelist = valuelist[0:-1]
    sqlstatement += "UPDATE " + TABLE_NAME + " SET " +valuelist + " WHERE ID = " +  "" + name + ""
    #print(sqlstatement)
    return sqlstatement


class UserDB():


    @staticmethod
    def GetUsers():
        print("starting")
        try:
            ServiceSQL.getConector().execute("SELECT Usuarios.ID,Usuarios.nombre,Usuarios.apellido_paterno,Usuarios.apellido_materno,Usuarios.IDtipoUsuario,Usuarios.fecha,Usuarios.telefono,Usuarios.correo,Roles.rol from Usuarios inner join Roles on Usuarios.IDtipoUsuario = Roles.ID")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            #data = []
            #print(row)
            #for r in row:
            #    data.append([x for x in r])

            #items = []
            #for item in row:
            #    items.append({'ID':item[0],'nombre':item[1],'apellido_materno':item[2],'apellido_paterno':item[3],'contrasena':item[4],'tipoUsuario':item[5],'fechaContratacion':item[6],'telefono':item[7],'correo':item[8]})


            #datos = json.dumps(items)


            rows = [x for x in row]
            cols = [x[0] for x in ServiceSQL.getConector().description]
            filas = []
            for row in rows:
                fila = {}
                for prop, val in zip(cols, row):
                    if isinstance(val, (datetime, date)):
                        fila[prop] = val.isoformat()
                    else:
                        fila[prop] = val

                filas.append(fila)

           
            datos = json.dumps(filas)
            #print(json.dumps(data))
            return datos
        except Exception as e:
            
            print(e)
            return 2

    

    @staticmethod
    def GetUser(name):
        
       
        try:
            ServiceSQL.getConector().execute("SELECT Usuarios.ID,Usuarios.nombre,Usuarios.apellido_paterno,Usuarios.apellido_materno,Usuarios.IDtipoUsuario,Usuarios.fecha,Usuarios.telefono,Usuarios.correo,Roles.rol,Usuarios.foto from Usuarios inner join Roles on Usuarios.IDtipoUsuario = Roles.ID where Usuarios.ID = " + name + "")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            
            
            if len(row) == 0:
                return 1
            
            rows = [x for x in row]
            cols = [x[0] for x in ServiceSQL.getConector().description]
            filas = []
            for row in rows:
                fila = {}
                for prop, val in zip(cols, row):
                    if isinstance(val, (datetime, date)):
                        fila[prop] = val.isoformat()
                    else:
                        fila[prop] = val

                filas.append(fila)

            #print(filas)

            datos = json.dumps(filas)
            
            #print(json.dumps(data))
            return datos
        except:
            print("Error de SQL")
            return 2


    
    @staticmethod
    def GetUserByName(name):
        
       
        try:
            ServiceSQL.getConector().execute("SELECT Usuarios.ID,Usuarios.nombre,Usuarios.apellido_paterno,Usuarios.apellido_materno,Usuarios.IDtipoUsuario,Usuarios.fecha,Usuarios.telefono,Usuarios.correo,Roles.rol,Usuarios.foto from Usuarios inner join Roles on Usuarios.IDtipoUsuario = Roles.ID where Usuarios.nombre = '" + name + "'")
            print("queried")
            row = ServiceSQL.getConector().fetchall()
            
            if len(row) == 0:
                return 1
            
            rows = [x for x in row]
            cols = [x[0] for x in ServiceSQL.getConector().description]
            filas = []
            for row in rows:
                fila = {}
                for prop, val in zip(cols, row):
                    if isinstance(val, (datetime, date)):
                        fila[prop] = val.isoformat()
                    else:
                        fila[prop] = val

                filas.append(fila)

            #print(filas)

            datos = json.dumps(filas)
            
            #print(json.dumps(data))
            return datos
        except:
            print("Error de SQL")
            return 2



    @staticmethod
    def postUser(usuario):
        try:
            #print(usuario)

            ServiceSQL.getConector().execute("SELECT count(*) from Usuarios where nombre = '" + usuario['nombre'] + "'")
            row = ServiceSQL.getConector().fetchall()
            #print(row)
            data = []
            
            for r in row:
                data.append([x for x in r])

          
            items = []
            for item in row:
                items.append(item[0])

           
            if items[0] == 0:
            
                
                sqlinsert = cmdinsert("Usuarios",usuario)
                #print(sqlinsert)
                ServiceSQL.getConector().execute(sqlinsert)
                ServiceSQL.getcnxn().commit()
          
                return 0
            else:
                return 1
        except Exception as e:
            print(e)
            return 2
        


    @staticmethod
    def putUser(usuario,name):
        #check if use exist
        
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuarios where ID = " + name + "")
            row = ServiceSQL.getConector().fetchall()
            
            if len(row) >= 0:

                #update user
                sqlupdate = cmdupdate("Usuarios",usuario,name)

                ServiceSQL.getConector().execute(sqlupdate)
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
    
        except Exception as e:
            print(e)
            return 2        
       
                

    @staticmethod
    def delUser(usuario):
        print(usuario)
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuarios where nombre = '" + usuario + "'")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            data = []
            
            for r in row:
                data.append([x for x in r])

          
            items = []
            for item in row:
                items.append(item[0])

                
            if item[0] > 0:

                #delete user

                ServiceSQL.getConector().execute("Delete from Usuarios WHERE nombre = '" + usuario + "'")
                ServiceSQL.getcnxn().commit()
                print('deleted')
                return 0
            else:
                return 1
    
        except:
            print('server error')
            return 2 
            
    
    @staticmethod
    def loginprev(usuario):
        try:
            
                   
            ServiceSQL.getConector().execute("select nombre,password from Usuarios where nombre = '" + usuario['nombre'] + "'")
            
            row = ServiceSQL.getConector().fetchall()
                    
            print(row[0][1])
            

            if len(row) == 0:
                return 1
                                 

            #if usuario['password'] == row[0][1]:
            if check_password_hash(row[0][1],usuario['password'])==True:
                return 0
            
            else:
                return 2
            
        except ValueError:
            print("error de transaccion")
            return 3
        


#INSERT INTO Usuario (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) 
#VALUES ('12312312', 'rody', 'vazquez', 'lopez','123456','administrador','2019-03-05','5567890098','rodrigo2020@hotmail.com');
