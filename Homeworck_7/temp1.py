### 1. Функция группового переименования файлов:
import os

def batch_rename_files(directory, desired_name, num_digits, original_extension, new_extension, name_range=(0, None)):
    file_counter = 1
    for file in os.listdir(directory):
        if file.endswith(original_extension):
            name_part = file[name_range[0]:name_range[1]] + desired_name if desired_name else ""
            new_name = f"{name_part}{file_counter:0{num_digits}d}.{new_extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            file_counter += 1

# Пример использования
directory = "/path/to/directory"
desired_name = "new_files"
num_digits = 3
original_extension = ".txt"
new_extension = "doc"
name_range = (3, 6)  # Использовать символы с 3 по 6 для имен файлов
batch_rename_files(directory, desired_name, num_digits, original_extension, new_extension, name_range)
