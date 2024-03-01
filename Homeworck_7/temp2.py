### 2. Создание пакета для работы с файлами:

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# rename_operations.py
import os

def batch_rename_files(directory, desired_name, num_digits, original_extension, new_extension, name_range=(0, None)):
    file_counter = 1
    for file in os.listdir(directory):
        if file.endswith(original_extension):
            name_part = file[name_range[0]:name_range[1]] + desired_name if desired_name else ""
            new_name = f"{name_part}{file_counter:0{num_digits}d}.{new_extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            file_counter += 1