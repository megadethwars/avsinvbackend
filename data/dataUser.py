from data.Service import ServiceSQL
import json

class UserDB():


    @staticmethod
    def executePost():
        print("starting")
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuario")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            data = []
            print(row)
            for r in row:
                data.append([x for x in r])

            items = []
            for item in row:
                items.append({'ID':item[0],'nombre':item[1],'apellido_materno':item[2],'apellido_paterno':item[3],'contrasena':item[4],'tipoUsuario':item[5],'fechaContratacion':item[6],'telefono':item[7],'correo':item[8]})


            datos = json.dumps(items)
            #print(json.dumps(data))
            return datos
        except:
            print("Error de SQL")
            return None


    
    @staticmethod
    def GetUser(name):
        
       
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuario where nombre = '" + name + "'")
            print("queried")
            row = ServiceSQL.getConector().fetchall()
            
            if len(row) == 0:
                return 1
            
            data = []
            items = []
            print(row)
            #for r in row:
            #    data.append([x for x in r])

            

            for item in row:
                items.append({'ID':item[0],'nombre':item[1],'apellido_materno':item[2],'apellido_paterno':item[3],'contrasena':item[4],'tipoUsuario':item[5],'fechaContratacion':item[6],'telefono':item[7],'correo':item[8]})

            objectouser = {
                "ID": item[0],
                "nombre": item[1],
                "apellido_materno": item[2],
                "apellido_paterno": item[3],
                "contrasena": item[4],
                "tipoUsuario": item[5],
                "fechaContratacion": item[6],
                "telefono": item[7],
                "correo": item[8]
            }

            datos = json.dumps(objectouser)
            
            #print(json.dumps(data))
            return datos
        except:
            print("Error de SQL")
            return None

        
        

    @staticmethod
    def postUser(usuario):
        try:
            #print(usuario)
            
            
            ServiceSQL.getConector().execute("INSERT INTO Usuario (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
            ServiceSQL.getcnxn().commit()


            return 0
        except ValueError:
            print("error de transaccion")
            return 2
        


    @staticmethod
    def putUser(usuario):
        #check if use exist
        print(usuario)
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuario where nombre = '" + usuario['nombre'] + "'")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            if len(row) >= 0:

                #update user

                ServiceSQL.getConector().execute("UPDATE Usuario SET apellido_materno = '" + usuario['apellido_materno'] + "', apellido_paterno = '" + usuario['apellido_paterno'] + "',tipoUsuario = '" + usuario['tipoUsuario'] + "',telefono = '" + usuario['telefono'] + "',correo = '" + usuario['correo'] + "'    WHERE nombre = '" + usuario['nombre'] + "'")
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
    
        except:
            print('server error')
            return 2        
       
                

    @staticmethod
    def delUser(usuario):
        print(usuario)
        try:
            ServiceSQL.getConector().execute("SELECT * from Usuario where nombre = '" + usuario + "'")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            if len(row) >= 0:

                #delete user

                ServiceSQL.getConector().execute("Delete from Usuario WHERE nombre = '" + usuario + "'")
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
            
                   
            ServiceSQL.getConector().execute("select nombre,contrasena from Usuario where nombre = '" + usuario['nombre'] + "'")
            
            row = ServiceSQL.getConector().fetchall()
                    
            print(row[0][1])
            

            if len(row) == 0:
                return 1
                                 

            if usuario['contrasena'] == row[0][1]:
                return 0
            
            else:
                return 2
            
        except ValueError:
            print("error de transaccion")
            return 3
        


#INSERT INTO Usuario (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) 
#VALUES ('12312312', 'rody', 'vazquez', 'lopez','123456','administrador','2019-03-05','5567890098','rodrigo2020@hotmail.com');
