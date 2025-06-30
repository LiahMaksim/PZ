#В двумерном списке найти суммы элементов каждого столбца и поместить их в новый массив. Выполнить замену элементов второй строки исходной матрицы на полученные суммы.

def process_matrix(matrix):
    column_sums = [sum(col) for col in zip(*matrix)]
    
    matrix[1] = column_sums
    
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

result_matrix = process_matrix(matrix)

print("\nМатрица после замены второй строки на суммы столбцов:")
for row in result_matrix:
    print(row)