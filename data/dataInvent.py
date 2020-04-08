from data.Service import ServiceSQL
import json
import traceback
from datetime import date, datetime

def cmdinsert(table,objeto):
    table = str(table)
    TABLE_NAME = table

    sqlstatement = ''

    keylist = "("
    valuelist = "("
    firstPair = True
    for key, value in objeto.items():
        if key !='ID' and key !='fecha'  and key!='lugar' and key!='Fecha' and key!='message' and key!='statuscode' and key!='Lugar':
            if not firstPair:
                keylist += ", "
                valuelist += ", "
            firstPair = False
            keylist += key
            
            if type(value) is str:
                valuelist += "'" + value + "'"
            
            elif value is None:
                
                valuelist += "'N/A'"
            
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
        if key !='ID' and key !='fecha'  and key!='lugar' and key!='Fecha' and key!='Lugar' and key!='message' and key!='statuscode':
            if type(value) is int:
                valuelist+=key + " = "+ str(value) + ","
            elif type(value) is str:
                valuelist+=key + " = "+ "'" + value + "'" + ","
            elif value is None:
                valuelist+=key + " = "+ "'N/A'" + ","

    
    valuelist = valuelist[0:-1]
    sqlstatement += "UPDATE " + TABLE_NAME + " SET " +valuelist + " WHERE ID = " +  "" + name + ""
    
    return sqlstatement

def cmdselect(argumentos,cols):
    select = ""

    select = str(select)

    select = "select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where "

    isfirst=False
    count = 0


    for column in argumentos:
       
        if column != "" and column != 'null' and column!=None:
            
            if isfirst==True:
                if type(column) is str:        
                    select+=" and " + cols[count] + " = '" + column + "' "
                else:
                    select+=" and " + cols[count] + " = " + column + ""
            else:   
                if type(column) is str:
                    select+="" + cols[count] + " = '" + column + "' " 
                else:
                    select+="" + cols[count] + " = " + column + "" 

            isfirst = True
        
        count=count + 1
    select+=" order by codigo"
    
    return select

class InventDB():


    @staticmethod
    def getDevices():
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID order by codigo")
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
                    #print(prop,val)
                    if isinstance(val, (datetime, date)):
                        fila[prop] = val.isoformat()
                    else:
                        fila[prop] = val
                    
                    #print(fila)

                filas.append(fila)

            
            datos = json.dumps(filas)
            
            return datos
        except Exception as e:
            print(e)
            return 2



    @staticmethod
    def getDevicesbycode(id):
        #print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.codigo= '" + id + "' order by codigo")
            #print("queried")
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
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbyname(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.producto= '" + id + "' ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbyID(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.ID= " + id + " ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2



    @staticmethod
    def getDevicesbymarca(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.marca= '" + id + "' ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2



    @staticmethod
    def getDevicesbymodelo(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.modelo= '" + id + "' ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbyserie(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.serie= '" + id + "' ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbyproveedor(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Dispositivos.ID,codigo,producto,marca,fecha,modelo,foto,cantidad,observaciones,IDlugar,pertenece,descompostura,costo,compra,serie,proveedor,Lugares.lugar,origen,Dispositivos.IDlugar from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.proveedor= '" + id + "' ")
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

            print(filas)
            datos = json.dumps(filas)
            
            return datos
        except ValueError:
            print('error sql')
            return 2


    @staticmethod
    def getDevicesbysearch(listaargs):
        print("starting")
        try:

            columnas = ["codigo","producto","fecha","marca","modelo","serie"]

            strsel =cmdselect(listaargs,columnas)

           

            ServiceSQL.getConector().execute(strsel)
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
                    #print(prop,val)
                    if isinstance(val, (datetime, date)):
                        fila[prop] = val.isoformat()
                    else:
                        fila[prop] = val
                    
                    #print(fila)

                filas.append(fila)

            
            datos = json.dumps(filas)
            
            return datos
        except Exception as e:
            print(e)
            return 2

    
    @staticmethod
    def GetDevice(id):
        
       
        try:
            ServiceSQL.getConector().execute("select * from Dispositivos inner join Lugares on Dispositivos.IDlugar = Lugares.ID where Dispositivos.ID= " + id + "")
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
            
            ServiceSQL.getConector().execute("SELECT count(*) from Dispositivos where codigo = '" + dispositivo['codigo'] + "'")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            data = []
            
            for r in row:
                data.append([x for x in r])

          
            items = []
            for item in row:
                items.append(item[0])


            if items[0]==0:
            
                strinsert = cmdinsert("Dispositivos",dispositivo)
            
                #print(strinsert)
                #ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
                ServiceSQL.getConector().execute(strinsert)
                ServiceSQL.getcnxn().commit()
                return 0

            else:
                return 1


            


            return 0
        except Exception as e:
            print(e)
            return 2
        


    @staticmethod
    def putDevice(dispositivo,id):
        #check if use exist
        
        try:
            ServiceSQL.getConector().execute("SELECT * from Dispositivos  where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
            #print(row)
            if len(row) >= 0:

                #update device

                strupdate = cmdupdate("Dispositivos",dispositivo,id)
                #print(strupdate)
                ServiceSQL.getConector().execute(strupdate)
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
    
        except Exception as e:
            print(e)
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
