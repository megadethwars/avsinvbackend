from data.Service import ServiceSQL
import json
import traceback

class TypemovesDB():

    @staticmethod
    def getmoves():
        try:
            ServiceSQL.getConector().execute("SELECT * from Moves")
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
                items.append({'ID':item[0],'tipomovimiento':item[1]})


            datos = json.dumps(items)
            #print(json.dumps(data))
            return datos
            
        except ValueError:
            print(ValueError)
            return 2


    @staticmethod
    def getMove(id):
        try:
            print("atarting")
            print(id)
            ServiceSQL.getConector().execute("SELECT * from Moves where ID = " + id + "")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            data = []
            
            for r in row:
                data.append([x for x in r])

            items = []
            for item in row:
                items.append({'ID':item[0],'tipomovimiento':item[1]})

            print(items)
            datos = json.dumps(items)
            return datos
            
        except ValueError:
            print(ValueError)
            return 2
            


    @staticmethod
    def postMove(objeto):
        print(objeto)
        try:
            cmdinsert = "insert into Moves values ('" + objeto['tipomovimiento'] + "')"
            print(cmdinsert)
            ServiceSQL.getConector().execute(cmdinsert)
            ServiceSQL.getcnxn().commit()
            return 0
        except Exception as e:
            print(e)
            return 2

    
    @staticmethod
    def putMove(id,objeto):
        try:
            print('starting')
            print(id)
            ServiceSQL.getConector().execute("SELECT count(*) from Moves where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
          
            data = []
            
            for r in row:
                data.append([x for x in r])

          
            items = []
            for item in row:
                items.append(item[0])

            print(items[0])

            if items[0] > 0:

                #update user
                print('updating')
                ServiceSQL.getConector().execute("UPDATE Moves SET tipomovimiento = '" + objeto['tipomovimiento'] + "' WHERE ID = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
            
        except ValueError:
            print(ValueError)
            return 2

    
    @staticmethod
    def deleteMove(id):
        try:
            ServiceSQL.getConector().execute("SELECT * from Moves where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            if len(row) > 0:

                #delete user

                ServiceSQL.getConector().execute("Delete from Moves WHERE iD = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('deleted')
                return 0
            else:
                return 1
        except ValueError:
            print(ValueError)
