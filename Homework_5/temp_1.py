### 1. Получение информации из абсолютного пути до файла:
import os

def get_file_info(file_path):
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension

# Пример использования
file_path = "/path/to/file/example.txt"
path, filename, extension = get_file_info(file_path)
print("Путь:", path)
print("Имя файла:", filename)
print("Расширение файла:", extension)