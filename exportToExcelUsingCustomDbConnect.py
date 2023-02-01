from mysql_reuseable_connect import Database
from mysql.connector import Error
import pandas.io.sql as sql

def exportToExcelUsingCUstomDbConnect():
    try:
        database = Database()
        df = sql.read_sql('SELECT * FROM programming_languages', database.connection)
        df.to_excel('myDummy.xlsx')
    except Error as e:
        print(e)
        
exportToExcelUsingCUstomDbConnect()