from data.Service import ServiceSQL
import json
import traceback
from datetime import date, datetime

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
        insertcmd+="'" + value + "',"
        cont2=cont2+1

    insertcmd=insertcmd[0:-1]
    insertcmd+=")"    

    print(insertcmd)
    return insertcmd



def strselect(argumentos,cols):
    select = ""

    select = str(select)

    select = "select Movimientos.ID,Movimientos.IDmovimiento,Movimientos.IDtipomov,Movimientos.IDusuario,Movimientos.fechamovimiento,Dispositivos.codigo,Dispositivos.producto,Dispositivos.serie,Dispositivos.marca,Dispositivos.modelo,Dispositivos.IDlugar,Usuarios.nombre,Lugares.Lugar,observacionesMov,tipomovimiento,fotomov1,fotomov2 from Movimientos inner join Dispositivos on Movimientos.IDdevice = Dispositivos.ID inner join Moves on Movimientos.IDtipomov = Moves.ID inner join Usuarios on Movimientos.IDusuario = Usuarios.ID inner join Lugares on Dispositivos.IDlugar = Lugares.ID where "

    isfirst=False
    count = 0


    for column in argumentos:
       
        if column != "" and column != 'null' and column!=None and column!='0':
            
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
    select+=" order by fechamovimiento"
    print(strselect)
    return select

    
def cmdinsert(table,objeto):
    table = str(table)
    TABLE_NAME = table

    sqlstatement = ''

    keylist = "("
    valuelist = "("
    firstPair = True
    for key, value in objeto.items():
        if key !='ID' and key !='fecha' and key!='fechamovimiento' and key!='lugar' and key!='codigo' and key!='producto' and key!='marca' and key!='modelo' and key!='nombre' and key!='Lugar' and key!='serie' and key!='statuscode' and key!='message' and key!='IDlugar' and key!='cantidad' and key!='tipomovimiento':
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
            
            elif value is None:
                print("nulo")
                valuelist += "'N/A'"
            
            else:
                valuelist += str(value)
            
    keylist += ")"
    valuelist += ")"

    sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist
    
    return sqlstatement

class HistorialDB():

    @staticmethod
    def getHistorial():
        print("starting")
        try:
            ServiceSQL.getConector().execute("select Movimientos.ID,Movimientos.IDmovimiento,Movimientos.IDtipomov,Movimientos.IDusuario,Movimientos.fechamovimiento,Dispositivos.codigo,Dispositivos.producto,Dispositivos.serie,Dispositivos.marca,Dispositivos.modelo,Dispositivos.IDlugar,Usuarios.nombre,Lugares.Lugar,observacionesMov,tipomovimiento,fotomov1,fotomov2 from Movimientos inner join Dispositivos on Movimientos.IDdevice = Dispositivos.ID inner join Moves on Movimientos.IDtipomov = Moves.ID inner join Usuarios on Movimientos.IDusuario = Usuarios.ID inner join Lugares on Dispositivos.IDlugar = Lugares.ID order by fechamovimiento")
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
    def getHistorialbysearch(listaargs):
        print("starting")
        try:

            columnas = ["IDmovimiento","IDtipomov","IDlugar","IDusuario","producto","fechamovimiento","modelo","marca","codigo","serie"]

            strsel =strselect(listaargs,columnas)

            #print(strsel)

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
    def postHistorial(movimiento):
        try:
            
            columns= []

            for r in ServiceSQL.getConector().columns(table='Movimientos'):
                
                columns.append(r.column_name)

            #print(columns)
            insert = cmdinsert("Movimientos",movimiento)
            #ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
            ServiceSQL.getConector().execute(insert)
            ServiceSQL.getcnxn().commit()



            return 0
        except Exception as e:
            print(e)
            return 2


    