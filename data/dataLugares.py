from data.Service import ServiceSQL
import json
import traceback

class LugarDB():

    @staticmethod
    def getLugares():
        try:
            ServiceSQL.getConector().execute("SELECT * from Lugares")
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
                items.append({'ID':item[0],'Lugar':item[1]})


            datos = json.dumps(items)
            #print(json.dumps(data))
            return datos
            
        except ValueError:
            print(ValueError)
            return 2


    @staticmethod
    def getLugar(id):
        try:
            print("atarting")
            print(id)
            ServiceSQL.getConector().execute("SELECT * from Lugares where ID = " + id + "")
            print("queried")
            row = ServiceSQL.getConector().fetchall()

            if len(row) == 0:
                return 1

            data = []
            
            for r in row:
                data.append([x for x in r])

            items = []
            for item in row:
                items.append({'ID':item[0],'Lugar':item[1]})

            print(items)
            datos = json.dumps(items)
            return datos
            
        except ValueError:
            print(ValueError)
            return 2
            


    @staticmethod
    def postLugar(objeto):
        print(objeto)
        try:
            ServiceSQL.getConector().execute("SELECT count(*) from Lugares where Lugar = '" + objeto['Lugar'] + "'")
            row = ServiceSQL.getConector().fetchall()
            #print(row)
            data = []
            
            for r in row:
                data.append([x for x in r])
        
            items = []
            for item in row:
                items.append(item[0])
         
            if items[0] == 0:

                cmdinsert = "insert into Lugares(Lugar) values ('" + objeto['Lugar'] + "')"
                print(cmdinsert)
                ServiceSQL.getConector().execute(cmdinsert)
                ServiceSQL.getcnxn().commit()
                return 0
            else:
                return 1
        except Exception as e:
            print(e)
            return 2

    
    @staticmethod
    def putLugar(id,objeto):
        try:
            print('starting')
            print(id)
            ServiceSQL.getConector().execute("SELECT count(*) from Lugares where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
          
                    
            items = []
            for item in row:
                items.append(item[0])

            print(items[0])

            if items[0] > 0:

                #update user
                print('updating')
                ServiceSQL.getConector().execute("UPDATE Lugares SET Lugar = '" + objeto['Lugar'] + "' WHERE ID = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('updated')
                return 0
            else:
                return 1
            
        except Exception as e:
            print(e)
            return 2

    
    @staticmethod
    def deleteLugar(id):
        try:
            ServiceSQL.getConector().execute("SELECT * from Lugares where ID = " + id + "")
            row = ServiceSQL.getConector().fetchall()
            print(row)
            data = []
            
            for r in row:
                data.append([x for x in r])

          
            items = []
            for item in row:
                items.append(item[0])

            print(items[0])
            if items[0] > 0:

                #delete user


                ServiceSQL.getConector().execute("Delete from Lugares WHERE iD = " + id + "")
                ServiceSQL.getcnxn().commit()
                print('deleted')
                return 0
            else:
                return 1
        except ValueError:
            print(ValueError)
