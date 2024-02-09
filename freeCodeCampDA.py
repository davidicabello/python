import pandas as pd
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# folder_path = r'D:\gitHub Repository\FreeCodeCamp-Pandas-Real-Life-Example\data'
# all_files = os.listdir(folder_path)
# csv_files = [f for f in all_files if f.endswith('.csv')]
# df_list= []
# print (csv_files)
sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])
print (sales.head())
# print(sales.shape)

# print (sales.info())

# print(sales.describe())

# sales['Unit_Cost'].describe()

# sales['Unit_Cost'].mean()

# sales['Unit_Cost'].median()

