import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.get(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data(2)

def create_data():
    data = {
        'name' : 'rohini',
        'roll' : 109,
        'city' : 'kisannagar'
    }

    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# create_data()

def update_data():
    data = {
        'id' : 3,
        'name' : 'amit',
        'roll' : 150,
        'city' : 'mumbai'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id' : 4,
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers,data = json_data)
    data = r.json()
    print(data)

delete_data()