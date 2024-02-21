### 2. Однострочный генератор словаря:
names = ["Alice", "Bob", "Charlie"]
rates = [100, 200, 150]
bonuses = ["10.25%", "15.50%", "12.75%"]

result_dict = {name: rate * float(bonus.replace("%", "")) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
print(result_dict)