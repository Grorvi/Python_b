### 1. Транспонирование матрицы:
def transpose_matrix(matrix):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed

# Пример использования
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)