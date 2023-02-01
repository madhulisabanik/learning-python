from mysql.connector import connect, Error

class Database(object):
    connection = None
    cursor = None
    
    def __init__(self):
        if Database.connection is None:
            try:
                Database.connection = connect(
                    host="localhost",
                    user="root",
                    password="password",
                    database="myTestDB",
                )
                Database.cursor = Database.connection.cursor()
            except Error as error:
                print("Error: Connection not established {}".format(error))
            else:
                print("Connection established")
                
        self.connection = Database.connection
        self.cursor = Database.cursor