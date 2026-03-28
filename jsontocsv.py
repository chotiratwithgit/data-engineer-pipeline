import json
import glob
import os
import pandas as pd 


# Load Raw Data
json_files = glob.glob("raw_brewery_data_*.json")  # Search for JSON files in the current directory that match the pattern "raw_brewery_data_*.json"

if json_files:

    filename = json_files[0]  # Select the first file found
    
    with open(filename, "r", encoding="utf-8") as file:

        raw_data = json.load(file)  # Load data from the JSON file

        print(f"Load Raw Data from File '{filename}' Successful!")
else :
    print("No JSON files found in the 'data' folder.")
    exit()

#Create Dataframe
df = pd.DataFrame(raw_data) 

# Choose colum to create
columns_to_keep = ['id', 'name', 'brewery_type', 'city', 'state', 'country']
df_cleaned = df[columns_to_keep]


#  Solve Missing Values

df_cleaned.loc[:, 'city'] = df_cleaned['city'].fillna('Unknown')

# Cleaned Data
print("\nCleaned Data:")
print(df_cleaned.head())

# Save To Csv
output_filename = "cleaned_breweries.csv"
df_cleaned.to_csv(output_filename, index=False, encoding="utf-8")

print(f"\nSave Cleaned Data to File '{output_filename}' Successful!")