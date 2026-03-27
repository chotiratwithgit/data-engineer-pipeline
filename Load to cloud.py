import pandas as pd
import boto3 
import os
from dotenv import load_dotenv

# Read the CSV 

input_filename = 'cleaned_breweries.csv' 
print(f"Reading data from {input_filename}...")
df = pd.read_csv(input_filename)


# Convert to parquet

parquet_filename = 'cleaned_data.parquet'
df.to_parquet(parquet_filename, engine='pyarrow', index=False)
print(f"Data converted successfully to {parquet_filename}.")


# Upload to cloud (AWS S3)

load_dotenv() # โหลดตัวแปรจาก .env

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'my-data-portfolio-chotirat-2026'


def upload_to_s3(file_name, bucket_name):
    print(f"Uploading {file_name} to S3 bucket '{bucket_name}' บน AWS...")

    try:
       
        s3_client = boto3.client(
            's3', 
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY  
        )
       
        
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(" Uploaded successfully to bucket!")
        
    except Exception as e:
        print(f" Error uploading file to S3: {e}")


upload_to_s3(parquet_filename, BUCKET_NAME)
                             
                             
                             
                             


