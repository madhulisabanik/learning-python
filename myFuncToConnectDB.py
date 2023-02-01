from mysql_reuseable_connect import Database
from mysql.connector import Error

def foo():
    try:
        database = Database()
        local_cursor = database.cursor
        local_cursor.execute("SELECT * FROM programming_languages")
        myresult = local_cursor.fetchall()
        for x in myresult:
            print(x)
    except Error as e:
        print(e)
        
foo()