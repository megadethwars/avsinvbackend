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
        if key !='ID' and key !='fecha' and key!='fechareporte' and key!='codigo' and key!='producto' and key!='marca' and key!='serie' and key!='nombre':
            if not firstPair:
                keylist += ", "
                valuelist += ", "
            firstPair = False
            keylist += key
            
            if type(value) is str:
                valuelist += "'" + value + "'"
            
            elif type(value) == None:
                print("nulo")
                valuelist += ""
            
            else:
                valuelist += str(value)
            
    keylist += ")"
    valuelist += ")"

    sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist
    
    return sqlstatement

class ReportDB():


    @staticmethod
    def getReport():
        print("starting")
        try:
            ServiceSQL.getConector().execute("select top 100 * from Reportes order by codigo")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1


            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'producto':item[2],'serie':item[3],'nombre':item[4],'marca':item[5],'modelo':item[6],'comentario':item[7],'foto':item[8]})


            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print(ValueError)
            return 2



    @staticmethod
    def getReportsbycode(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute(" select * from Reportes where codigo = '" + id + "' ")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            
            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'producto':item[2],'serie':item[3],'nombre':item[4],'marca':item[5],'modelo':item[6],'comentario':item[7],'foto':item[8]})


            reportedevice = {
                "ID": item[0],
                "codigo": item[1],
                "producto": item[2],
                "serie": item[3],
                "nombre": item[4],
                "marca": item[5],
                "modelo": item[6],
                "comentario": item[7],
                "foto": item[8]
                
            }

            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print('error sql')
            return 2




    @staticmethod
    def getReportsbyname(id):
        print("starting")
        try:
            ServiceSQL.getConector().execute(" select * from Reportes where producto = '" + id + "' ")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            
            items = []
            for item in row:
                
                items.append({'ID':item[0],'codigo':item[1],'producto':item[2],'serie':item[3],'nombre':item[4],'marca':item[5],'modelo':item[6],'comentario':item[7],'foto':item[8]})


            reportedevice = {
                "ID": item[0],
                "codigo": item[1],
                "producto": item[2],
                "serie": item[3],
                "nombre": item[4],
                "marca": item[5],
                "modelo": item[6],
                "comentario": item[7],
                "foto": item[8]
                
            }

            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print('error sql')
            return 2

    
        

    @staticmethod
    def postReport(reporte):
        try:
            insert = cmdinsert("Reportes",reporte)
            #ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
            ServiceSQL.getConector().execute(insert)
            ServiceSQL.getcnxn().commit()

            return 0
        except Exception as e:
            print(e)
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
            