import os
import kaggle 
import pandas as pd

# Specify the directory path you want to list
directory = '/users/kramchurn/.kaggle/'

# List all files and directories in the specified directory
files_and_directories = os.listdir(directory)

# Print each item in the list
for item in files_and_directories:
    print(item)

kaggle.api.authenticate()

kaggle.api.dataset_download_files('mayankanand2701/zomato-stock-price-dataset',path='.',unzip=True)
#tells you the file names in the kaggle directory
print(kaggle.api.dataset_list_files('mayankanand2701/zomato-stock-price-dataset').files)

kaggle.api.dataset_metadata('mayankanand2701/zomato-stock-price-dataset',path='.')
df = pd.read_csv('/users/kramchurn/Desktop/notebook part 2/python 2023/Zomato Dataset.csv')
