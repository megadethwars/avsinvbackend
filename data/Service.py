import pyodbc

class ServiceSQL(object):

    cursor = None

    Isconnected = False
    conector = None

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
            print("error de conexion")
        

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
        try:
            server = 'inventarioavs.database.windows.net'
            database = 'inventarioavs'
            username = 'forrerunner97'
            password = 'Asterisco97'
            driver= '{ODBC Driver 17 for SQL Server}'
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
            conector = cnxn.cursor()
            
            print("already connected")     
            
        except expression as identifier:
            print(identifier)

    @staticmethod
    def getConector():
        return conector        

        

