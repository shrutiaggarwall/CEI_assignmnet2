# Write a Python program that write data in csv file using Pandas of ISS location with timestamp min 100 records
# use this url to get the data of ISS
# ( url : http://api.open-notify.org/iss-now.json)

import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"
data = []
max_retries = 3

for _ in range(100):
    success = False
    retries = 0
    
    while not success and retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()
            latitude = json_data["iss_position"]["latitude"]
            longitude = json_data["iss_position"]["longitude"]
            timestamp = json_data["timestamp"]
            
            data.append({
                "timestamp": timestamp,
                "latitude": latitude,
                "longitude": longitude
            })
            
            print(f"Record {_+1}: Timestamp: {timestamp}, Latitude: {latitude}, Longitude: {longitude}")
            
            success = True  
            
        except requests.exceptions.RequestException as e:
            retries += 1
            print(f"Attempt {retries} failed: {e}")
            time.sleep(1)  
    
    if not success:
        print(f"Failed to retrieve data after {max_retries} attempts. Exiting.")
        break

df = pd.DataFrame(data)

df.to_csv("iss_location_data.csv", index=False)

print("Data collection complete. The data has been written to 'iss_location_data.csv'.")