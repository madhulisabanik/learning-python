# import openpyxl
from pymysql import*
import pandas.io.sql as sql

con = connect(user="root",password="password",host="localhost",database="myTestDB")

df = sql.read_sql('SELECT * FROM programming_languages', con)

print(df)

df.to_excel('myDummy.xls')