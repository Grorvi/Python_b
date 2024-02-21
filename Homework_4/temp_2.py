### 2. Создание словаря с ключевыми параметрами:
def dict_from_keywords(**kwargs):
    result_dict = {str(key): value for key, value in kwargs.items()}
    return result_dict

# Пример использования
kwargs_dict = dict_from_keywords(name='Alice', age=30, city='Wonderland')
print(kwargs_dict)