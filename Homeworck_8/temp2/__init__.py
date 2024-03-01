from file_formats import json_operations, csv_operations, pickle_operations

# Пример работы с файлами JSON
data = {"name": "Alice", "age": 30}
json_operations.write_json("data.json", data)
loaded_data = json_operations.read_json("data.json")
print(loaded_data)

# Пример работы с файлами CSV
data_csv = [["Alice", 30], ["Bob", 25]]
csv_operations.write_csv("data.csv", data_csv)
loaded_data_csv = csv_operations.read_csv("data.csv")
print(loaded_data_csv)

# Пример работы с файлами Pickle
data_pickle = [1, 2, 3, 4, 5]
pickle_operations.write_pickle("data.pkl", data_pickle)
loaded_data_pickle = pickle_operations.read_pickle("data.pkl")
print(loaded_data_pickle)