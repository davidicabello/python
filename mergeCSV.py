# IMPORT PANDAS
import pandas as pd
import csv
import os


# check to delete files
file_to_delete = r'Data/all_data.csv'
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
print(f'File deleted {file_to_delete}')
#add file container folder
folder_csv_path = r'Data/Sales_Data'
#get all csv
all_csv_files = [file for file in os.listdir(folder_csv_path)]
#check only csv files
all_csv_files = [file for file in all_csv_files if file.endswith('.csv')]
# concatenate all csv files
df_csv_files = pd.concat(
    [pd.read_csv(os.path.join(folder_csv_path, file)) for file in all_csv_files])
#save new file 
df_csv_files.to_csv(r'Data/all_data.csv', index=False)
#print result
print(df_csv_files)