#Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1 + A + A2 + A3 + ... + AN

def front(A, N):
    total_sum = 0
    current_term = 1
    for i in range(N + 1):
        total_sum += current_term
        current_term *= A
    return total_sum
try:
    A = int(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N (>0): "))
    if N > 0:
        result = front(A, N)
        print(f"Сумма: {result} ")
    else:
        print("N должно быть больше 0.")
except ValueError:
    print("Ошибка: Пожалуйста, введите корректные значения. A должно быть вещественным числом, а N - целым числом.")