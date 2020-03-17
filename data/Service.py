import pyodbc
import time


class ServiceSQL(object):

    cursor = None

    Isconnected = False
    conector = None
    cnxn = None

    def __init__(self):
        self._bar = 10
        self.isCon = False
        global cursor 
        try:

            server = 'inventarioavs.database.windows.net'
            database = 'inventarioavs'
            username = 'forrerunner97'
            password = 'Asterisco97'
            driver= '{ODBC Driver 17 for SQL Server}'
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
            cursor = cnxn.cursor()
            
            print("already connected")     
            self.isCon = True   
        except:
            self.isCon = False 
            print("error de conexion")
        
    @staticmethod
    def reconnect():
        global Isconnected
        global conector
        global cnxn
        while True:
            time.sleep(1800)
            try:
                print('reconectando')
                server = 'inventarioavs.database.windows.net'
                database = 'inventarioavs'
                username = 'forrerunner97'
                password = 'Asterisco97'
                driver= '{ODBC Driver 17 for SQL Server}'
                cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
                conector = cnxn.cursor()
                
                print("already connected")     
                Isconnected = True
            except:
                Isconnected = False
                print("error de conexion")


    def reconncetOnce():
        global Isconnected
        global conector
        global cnxn
        
        time.sleep(1)
        try:
            print('reconectando')
            server = 'inventarioavs.database.windows.net'
            database = 'inventarioavs'
            username = 'forrerunner97'
            password = 'Asterisco97'
            driver= '{ODBC Driver 17 for SQL Server}'
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
            conector = cnxn.cursor()
            
            print("already connected")     
            Isconnected = True
            return Isconnected
        except:
            Isconnected = False
            print("error de conexion")
            return Isconnected

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value

    @bar.deleter
    def bar(self):
        self._bar = None # for instance
   

    property
    def isCon(self):
        return self.isCon

    
   
    def GetConnection(self):
        return cursor


    @staticmethod
    def InitConexion():
        global Isconnected
        global conector
        global cnxn
        try:
            server = 'inventarioavs.database.windows.net'
            database = 'inventarioavs'
            username = 'forrerunner97'
            password = 'Asterisco97'
            driver= '{ODBC Driver 17 for SQL Server}'
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
            conector = cnxn.cursor()
            
            print("already connected")     
            
        except:
            print("error de conexion")

    @staticmethod
    def getConector():
        return conector      

    @staticmethod
    def getcnxn():
        return cnxn  

        

