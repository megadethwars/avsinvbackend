from data.Service import ServiceSQL
import json


class RoleDB():

    @staticmethod
    def getRoles():
        try:
            ServiceSQL.getConector().execute("SELECT * from Roles")
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
                items.append({'ID':item[0],'rol':item[1]})


            datos = json.dumps(items)
            #print(json.dumps(data))
            return datos
            
        except ValueError:
            print(ValueError)
            return 2


    @staticmethod
    def getRole(id):
        try:
            print("atarting")
            print(id)
            ServiceSQL.getConector().execute("SELECT * from Roles where ID = " + id + "")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            data = []
            
            for r in row:
                data.append([x for x in r])

            items = []
            for item in row:
                items.append({'ID':item[0],'rol':item[1]})

            print(items)
            datos = json.dumps(items)
            return datos
            
        except ValueError:
            print(ValueError)
            return 2
            


    @staticmethod
    def postRole(objeto):
        print(objeto)
        try:
            cmdinsert = "insert into Roles values ('" + objeto['rol'] + "')"
            print(cmdinsert)
            ServiceSQL.getConector().execute(cmdinsert)
            ServiceSQL.getcnxn().commit()
            return 0
        except ValueError:
            print(ValueError)
            return 2

    
    @staticmethod
    def putRole(id,objeto):
        try:
            print('starting')
            print(id)
            ServiceSQL.getConector().execute("SELECT count(*) from Roles where ID = " + id + "")
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
                ServiceSQL.getConector().execute("UPDATE Roles SET rol = '" + objeto['rol'] + "' WHERE ID = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
            
        except ValueError:
            print(ValueError)
            return 2

    
    @staticmethod
    def deleteRole(id):
        try:
            ServiceSQL.getConector().execute("SELECT * from Roles where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            if len(row) > 0:

                #delete user

                ServiceSQL.getConector().execute("Delete from Roles WHERE iD = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('deleted')
                return 0
            else:
                return 1
        except ValueError:
            print(ValueError)
