import csv

def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def read_csv(file_name):
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data