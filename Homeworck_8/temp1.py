### 2. Функция рекурсивного обхода директории и сохранения результатов в разные файловые форматы:
import os
import json
import csv
import pickle

def get_directory_info(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        total_size = dir_size
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            total_size += sum(os.path.getsize(os.path.join(dir_path, file)) for file in os.listdir(dir_path))
        result.append({
            "path": root,
            "type": "directory",
            "total_size": total_size
        })
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                "path": file_path,
                "type": "file",
                "size": file_size
            })
    
    # Сохранение результатов в различных форматах
    with open("directory_info.json", "w") as json_file:
        json.dump(result, json_file, indent=4)
    
    with open("directory_info.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["path", "type", "size"])
        for item in result:
            csv_writer.writerow([item.get("path"), item.get("type"), item.get("size", item.get("total_size"))])
    
    with open("directory_info.pickle", "wb") as pickle_file:
        pickle.dump(result, pickle_file)

# Пример использования
directory = "/path/to/directory"
get_directory_info(directory)