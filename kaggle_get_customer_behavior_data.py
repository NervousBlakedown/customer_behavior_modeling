# Imports
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# directory to store datasets
download_dir = "D:\\datasets\\github_customer_behavior_data"

# Initialize Kaggle API with manual credentials
api = KaggleApi()
api.authenticate()

# Dataset identifier from Kaggle
print()
dataset = 'imakash3011/customer-personality-analysis'
print()

# download dataset
api.dataset_download_files(dataset, path = download_dir, unzip = True)

# Optional: List of CSV files from Kaggle dataset source
files_of_interest = ['marketing_campaign.csv']

# Ensure files exist in the directory
for file_name in files_of_interest:
    file_path = os.path.join(download_dir, file_name)
    if os.path.exists(file_path):
        print(f'{file_name} has been downloaded successfully.')
    else:
        print(f'{file_name} is missing.')

print()
print("Download and extraction complete.  Have a great day, Blake, you handsome devil.")