import json
import requests

def send_data(data):
    url = "http://127.0.0.1:8000/smartphone/add/"
    r = requests.post(url, json=data)
    return r.status_code

with open('db.json', 'r') as file:
    data = json.load(file)

ls = ['Apple', 'Huawei', 'Nokia', 'Oppo', 'Samsung', 'Vivo']
for item in ls:
    element = data[item]
    for i, v in element.items():
        print(send_data(v))
        