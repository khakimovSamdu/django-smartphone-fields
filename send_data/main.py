import json
import requests
import random

def send_data(data):
    url = "http://127.0.0.1:8000/smartphone/add/"
    r = requests.post(url, json=data)
    return r.status_code

with open('db.json', 'r') as file:
    data = json.load(file)

ls = ['Apple', 'Huawei', 'Nokia', 'Oppo', 'Samsung', 'Vivo']
item = random.choice(ls)
element = data[item]
rand_ls = []
for i, v in element.items():
    rand_ls.append(v)
print(random.choice(rand_ls))
print(send_data(random.choice(rand_ls)))