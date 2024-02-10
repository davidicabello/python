import pandas as pd
import mysql.connector
import os

# CONNECT TO THE DB
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='asdqwe123',
    database='practicas_sql'
)
# CREATE A CURSOR OBJECT
cursor = connection.cursor()

# READ THE CSV FILE
merged_df = pd.read_csv(r'Data/Sales_Data/sales_data_combined.csv')
# TABLE NAME
table_name = 'sales_data_combined'

# CREATE TABLE IN MYSQL
cursor.execute(f"CREATE TABLE {table_name} ({', '.join(
    [f'`{col}` VARCHAR(255)' for col in merged_df.columns])})")

# INSERT DATA ROWS
for _, row in merged_df.iterrows():
    columns = ', '.join([f"`{col}`" for col in merged_df.columns])
    values = ', '.join(['%s' for _ in merged_df.columns])
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    try:
        cursor.execute(insert_query, tuple(row))
    except mysql.connector.Error as err:
        print(f"Error: {err}, Query: {insert_query}, Row: {row}")

# CONFIRM CHANGES
connection.commit()

# CLOSE CONNECTION
cursor.close()
connection.close()