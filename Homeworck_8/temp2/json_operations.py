import json

def write_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def read_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data