#В двумерном списке найти минимальный элемент в предпоследней строке.

def find_min_in_penultimate_row(matrix):
    if len(matrix) < 2:
        return None
    
    penultimate_row = matrix[-2]
    return min(penultimate_row)

matrix = [
    [5, 9, 2],
    [8, 3, 1],
    [4, 7, 6],
    [0, 2, 5]
]

print("Матрица:")
for row in matrix:
    print(row)

min_value = find_min_in_penultimate_row(matrix)
print("\nМинимальный элемент в предпоследней строке:", min_value)