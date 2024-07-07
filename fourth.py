# Write a Python program using the requests module to send a GET request to a given below URL API endpoint and print the json response
# (Url : http://api.open-notify.org/iss-now.json

import json
import requests
url="http://api.open-notify.org/iss-now.json"

headers={

 "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"

}

respose = requests.get(url,headers=headers)
print(respose)
print(respose.text)
