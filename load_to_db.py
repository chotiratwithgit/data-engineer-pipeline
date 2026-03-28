import pandas as pd
import psycopg2
import psycopg2.extras
import os


def load_data_to_db() :
    conn = None
    cursor = None

    try :
        print ("Loading data to database...")

        bucket_name = os.getenv('BUCKET_NAME') # get data from s3
        file_path = f"s3://{bucket_name}/cleaned_data.parquet"

        df = pd.read_parquet(file_path)  # read data from parquet file
        print (f"Data loaded from {len(df)} rows")

        df = df.where (pd.notnull(df), None)  # replace NaN with None 

        data_tuples = [tuple(x) for x in df.to_numpy()]   # convert dataframe to list of tuples

        db_url = os.getenv('DATABASE_URL')  # get database url 
        conn  = psycopg2.connect(db_url)  # connect to database
        cursor = conn.cursor()  # create cursor

# upsert query
        insert_query = """
        INSERT INTO breweries (id, name, berewery_type, street, city, state, postal_code, country, longitude , latitude)
        VALUES %s
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            berewery_type = EXCLUDED.berewery_type,
            street = EXCLUDED.street,
            city = EXCLUDED.city,
            state = EXCLUDED.state,
            postal_code = EXCLUDED.postal_code,
            country = EXCLUDED.country,
            longitude = EXCLUDED.longitude,
            latitude = EXCLUDED.latitude,
        """
           
        psycopg2.extras.execute_values(cursor, insert_query, data_tuples)  # execute query
        conn.commit() 
        print ("Data loaded successfully")


    except Exception as e:
        print (f"Error loading data: {e}")
        if conn:
            conn.rollback()
            print(" Rollback completed.")

    finally:
        if cursor:
            cursor.close()  # close cursor
        if conn:
            conn.close()  # close connection

if __name__ == "__main__" :
        load_data_to_db()






