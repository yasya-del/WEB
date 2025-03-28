import requests
import json


address = f"http://127.0.0.1:5000"

response = requests.get(address)
data_serv = response.json()
print(data_serv)
with open('p.json') as p_file:
    data_serv = json.load(p_file)
    print(data_serv)