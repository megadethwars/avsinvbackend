from data.Service import ServiceSQL
import json

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