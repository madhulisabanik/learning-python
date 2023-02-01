# from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        # user=input("Enter username: "),
        # password=getpass("Enter password: "),
        user="root",
        password="password",
        database="myTestDB",
    ) as connection:
        # print(connection)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM programming_languages")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
except Error as e:
    print(e)