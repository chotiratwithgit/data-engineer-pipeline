import json
import pandas as pd  # นำเข้า Pandas และตั้งชื่อเล่นสั้นๆ ว่า pd


# Load Raw Data

filename = "raw_brewery_data_260327.json" 

with open(filename, "r", encoding="utf-8") as file:
    raw_data = json.load(file) #  data json to python dict

print(f"Load Raw Data {len(raw_data)} Rows")

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