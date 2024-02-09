# IMPORT PANDAS
import pandas as pd
import csv
import os
import mysql.connector


# DIDN'T WORK
# READ THE CSV FILES INTO DRATA FRAMES
separator = ','
dataFrameOne = pd.read_csv(
    'Data/csvNovedadesene22del01al10.csv', sep=separator)
print(dataFrameOne.head())
