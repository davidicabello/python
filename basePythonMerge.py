# IMPORT PANDAS
import pandas as pd
import csv
import os
import mysql.connector


# DIDN'T WORK
# READ THE CSV FILES INTO DRATA FRAMES

csv_file_path= 'Data/csvNovedadesene22del01al10.csv'
dataFrameOne = pd.read_csv(csv_file_path,skiprows=range(1,4))
print(dataFrameOne)