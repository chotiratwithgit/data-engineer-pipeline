import requests
import json
import datetime
# Get API Data
def extract_brewery_data(per_page= 10) :
    url =f"https://api.openbrewerydb.org/v1/breweries?per_page={per_page}"

#  Go to exception if there is error in the request
    try : 
        print( f"Getting API: {per_page} items per page" )
        response = requests.get(url)
        
        response.raise_for_status()  # Check if the request was successful (status code 200)
        
        data = response.json()  #  JSON to Python dict
        print("successfully got data from API")
        return data
    
    except Exception as e:
        print(f"Error Getting data: {e}")
        return None
    
# Create function to save data to file
def save_raw_data(data_to_save, filename):
    if data_to_save != None:# Check if there is data to save

        # Open a file in write mode 
        with open(filename, "w",encoding="utf-8") as file:
            
            # Convert Python data to JSON and save to file
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)
        print(f"Data saved to file {filename} successfully!")
    else :
        print("No data to save")

# Main function to execute the code
if __name__ == "__main__":
    raw_data = extract_brewery_data(per_page=200)  # 

   # Generate file name with today's date
    today_date = datetime.datetime.now().strftime("%y%m%d") 
    file_name = f"raw_brewery_data_{today_date}.json"  
    
    # save file
    save_raw_data(raw_data,filename=file_name)