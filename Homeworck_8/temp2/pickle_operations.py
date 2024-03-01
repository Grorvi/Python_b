import pickle

def write_pickle(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)

def read_pickle(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data