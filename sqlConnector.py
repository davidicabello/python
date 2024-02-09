import pandas as pd
import os
import mysql.connector

# DB SQL-BOLT

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="asdqwe123",
    database="practicas_sql"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT title FROM movies")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
