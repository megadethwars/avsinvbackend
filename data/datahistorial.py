from data.Service import ServiceSQL
import json


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

    select = "select * from Movimientos where "

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

    print(select)
    return select

    

class HistorialDB():

    @staticmethod
    def getHistorial():
        print("starting")
        try:
            ServiceSQL.getConector().execute("select top 100 * from Movimientos order by fecha")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            columns= []
            
            for r in ServiceSQL.getConector().columns(table='Movimientos'):               
                columns.append(r.column_name)
            
            items = []

            movobj = {}

                                
            for item in row:
                cont = 0
                movobj = {}
                for column in columns:
                    movobj[column] = item[cont]
                    cont=cont+1

                items.append(movobj)      

            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print(ValueError)
            return 2

    
    @staticmethod
    def getHistorialbysearch(listaargs):
        print("starting")
        try:

            columnas = ["movimiento","lugar","usuario","producto","fecha","modelo","marca","codigo","serie"]

            strsel =strselect(listaargs,columnas)



            ServiceSQL.getConector().execute(strsel)
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            columns= []
            
            for r in ServiceSQL.getConector().columns(table='Movimientos'):               
                columns.append(r.column_name)
            
            items = []

            movobj = {}

                                
            for item in row:
                cont = 0
                movobj = {}
                for column in columns:
                    movobj[column] = item[cont]
                    cont=cont+1

                items.append(movobj)      

            datos = json.dumps(items)
            
            return datos
        except ValueError:
            print(ValueError)
            return 2
    

    @staticmethod
    def postHistorial(movimiento):
        try:
            

            columns= []


            for r in ServiceSQL.getConector().columns(table='Movimientos'):
                
                columns.append(r.column_name)

            print(columns)
            cmdinsert = strinsert("Movimientos",columns,movimiento)
            #ServiceSQL.getConector().execute("INSERT INTO InventDB (ID,nombre,apellido_materno,apellido_paterno,contrasena,tipoUsuario,fechaContratacion,telefono,correo) VALUES ('" + usuario['ID'] + "','" + usuario['nombre'] + "','" + usuario['apellido_materno'] + "','" + usuario['apellido_paterno'] + "','" + usuario['contrasena'] + "','" + usuario['tipoUsuario'] + "','" + usuario['fechaContratacion'] + "','" + usuario['telefono'] + "','" + usuario['correo'] + "')")
            ServiceSQL.getConector().execute(cmdinsert)
            ServiceSQL.getcnxn().commit()


            return 0
        except:
            print('error de sql')
            return 2


    