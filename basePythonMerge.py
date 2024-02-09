# IMPORT PANDAS
import pandas as pd
import csv
import os


# DIDN'T WORK
# READ THE CSV FILES INTO DRATA FRAMES
separator = ',"'
dataFrameOne = pd.read_csv('D:\PYTHONSTUFF\csv\combined_file.csv',sep=separator)

print (dataFrameOne)