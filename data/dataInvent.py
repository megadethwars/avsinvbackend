from data.Service import ServiceSQL
import json

class InventDB():


    @staticmethod
    def getDevices():
        print("starting")
        try:
            ServiceSQL.getConector().execute(" select top 100 * from InventDB order by codigo ")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            data = []
            #print(row)
            for r in row:
                data.append([x for x in r])

            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'nombre':item[2],'marca':item[3],'Fecha':item[4],'modelo':item[5],'foto':item[6],'cantidad':item[7],'origen':item[8],'observaciones':item[9],'lugar':item[10],'pertenece':item[11],'descompostura':item[12],'costo':item[13],'compra':item[14],'serie':item[15],'proveedor':item[16]  })


            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print(ValueError)
            return 2



    @staticmethod
    def getDevicesbycode(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute(" select * from InventDB where codigo = '" + id + "' ")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'nombre':item[2],'marca':item[3],'Fecha':item[4],'modelo':item[5],'foto':item[6],'cantidad':item[7],'origen':item[8],'observaciones':item[9],'lugar':item[10],'pertenece':item[11],'descompostura':item[12],'costo':item[13],'compra':item[14],'serie':item[15],'proveedor':item[16]  })

            objectodevice = {
                "ID": item[0],
                "codigo": item[1],
                "nombre": item[2],
                "marca": item[3],
                "Fecha": item[4],
                "modelo": item[5],
                "foto": item[6],
                "cantidad": item[7],
                "origen": item[8],
                "observaciones": item[9],
                "lugar": item[10],
                "pertenece": item[11],
                "descompostura": item[12],
                "costo": item[13],
                "compra": item[14],
                "serie": item[15],
                "proveedor": item[16]
                
            }

            datos = json.dumps(objectodevice)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbyname(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute(" select * from InventDB where nombre = '" + id + "' ")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'nombre':item[2],'marca':item[3],'Fecha':item[4],'modelo':item[5],'foto':item[6],'cantidad':item[7],'origen':item[8],'observaciones':item[9],'lugar':item[10],'pertenece':item[11],'descompostura':item[12],'costo':item[13],'compra':item[14],'serie':item[15],'proveedor':item[16]  })

            objectodevice = {
                "ID": item[0],
                "codigo": item[1],
                "nombre": item[2],
                "marca": item[3],
                "Fecha": item[4],
                "modelo": item[5],
                "foto": item[6],
                "cantidad": item[7],
                "origen": item[8],
                "observaciones": item[9],
                "lugar": item[10],
                "pertenece": item[11],
                "descompostura": item[12],
                "costo": item[13],
                "compra": item[14],
                "serie": item[15],
                "proveedor": item[16]
                
            }

            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    
    @staticmethod
    def GetDevice(id):
        
       
        try:
            ServiceSQL.getConector().execute("SELECT * from InventDB where codigo = '" + id + "'")
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
    def postDevice(dispositivo):
        try:
            print(dispositivo['ID'])
            
            
            #ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
            ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,codigo,nombre,marca,Fecha,modelo,foto,cantidad,origen,observaciones,lugar,pertenece,descompostura,costo,compra,serie,proveedor) VALUES   ('" + dispositivo['ID'] + "','" + dispositivo['codigo'] + "','" + dispositivo['nombre'] + "','" + dispositivo['marca'] + "','" + dispositivo['Fecha'] + "','" + dispositivo['modelo'] + "','" + dispositivo['foto'] + "','" + dispositivo['cantidad'] + "','" + dispositivo['origen'] + "','" + dispositivo['observaciones'] + "','" + dispositivo['lugar'] + "','" + dispositivo['pertenece'] + "','" + dispositivo['descompostura'] + "','" + dispositivo['costo'] + "','" + dispositivo['compra'] + "','" + dispositivo['serie'] + "','" + dispositivo['proveedor'] + "')")
            ServiceSQL.getcnxn().commit()


            return 0
        except ValueError:
            print(ValueError)
            return 2
        


    @staticmethod
    def putDevice(dispositivo):
        #check if use exist
        
        try:
            ServiceSQL.getConector().execute("SELECT * from InventDB where nombre = '" + dispositivo['codigo'] + "'")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            if len(row) >= 0:

                #update user

                ServiceSQL.getConector().execute("UPDATE InventDB SET codigo = '" + dispositivo['codigo'] + "',nombre = '" + dispositivo['nombre'] + "',marca = '" + dispositivo['marca'] + "',foto = '" + dispositivo['foto'] + "',cantidad = '" + dispositivo['cantidad'] + "',origen = '" + dispositivo['origen'] + "',observaciones = '" + dispositivo['observaciones'] + "',lugar = '" + dispositivo['lugar'] + "',pertenece = '" + dispositivo['pertenece'] + "',descompostura = '" + dispositivo['descompostura'] + "',costo = '" + dispositivo['costo'] + "',compra = '" + dispositivo['compra'] + "', serie = '" + dispositivo['serie'] + "',proveedor = '" + dispositivo['proveedor'] + "'      WHERE ID = '" + dispositivo['ID'] + "'")
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
    
        except:
            print('server error')
            return 2        
       
                

    @staticmethod
    def delDevice(codigo):
        print(codigo)
        try:
            ServiceSQL.getConector().execute("SELECT * from InventDB where codigo = '" + codigo + "'")
            row = ServiceSQL.getConector().fetchall()
            print(len(row))
            if len(row) > 0:

                #delete user

                ServiceSQL.getConector().execute("Delete from InventDB WHERE codigo = '" + codigo + "'")
                ServiceSQL.getcnxn().commit()
                print('deleted')
                return 0
            else:
                return 1
    
        except:
            print('server error')
            return 2 
            
    
    
        


#INSERT INTO Usuario (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) 
#VALUES ('12312312', 'rody', 'vazquez', 'lopez','123456','administrador','2019-03-05','5567890098','rodrigo2020@hotmail.com');
