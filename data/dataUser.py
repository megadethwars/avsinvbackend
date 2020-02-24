from ServiceDB import ServiceSQL
import json

class UserDB():


    @staticmethod
    def executePost():
        ServiceSQL.getConector().execute("SELECT * from Usuario where nombre = 'leon'")
        row = ServiceSQL.getConector().fetchall()
        data = []

        for r in row:
            data.append([x for x in r])

        json.dumps(data)
        print(json.dumps(data))
        




