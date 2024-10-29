def sum_series(A, N):
    total_sum = 0
    current_term = 1
    for i in range(N + 1):
        total_sum += current_term
        current_term *= A
    return total_sum
A = int(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (>0): "))
if N > 0:
    result = sum_series(A, N)
    print(f"Сумма: {result} ")
else:
    print(f"N должно быть больше 0.")