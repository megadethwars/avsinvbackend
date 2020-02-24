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
            data = []
            print("get rows")
            for r in row:
                data.append([x for x in r])

            datos = json.dumps(data)
            print(json.dumps(data))
            return datos
        except:
            print("Error de SQL")
            return None

        
        




