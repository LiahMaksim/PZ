#Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2, AN-1, A3, AN-2, ….

def rearrange_list(A):
    N = len(A)
    result = []
    for i in range((N + 1) // 2):
        result.append(A[i])
        if i != N - i - 1:
            result.append(A[N - i - 1])
    return result

A = [1, 2, 3, 4, 5, 6, 7, 8]
print(rearrange_list(A))