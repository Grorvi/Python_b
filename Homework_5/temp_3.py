### 3. Генератор чисел Фибоначчи:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci_gen))