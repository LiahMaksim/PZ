#Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K. Найти целое число K — показатель этой степени.

import math
def front(N):
    if N <= 0 or (N & (N - 1)) != 0:
        raise ValueError("N должно быть положительным и являться степенью двойки.")
    K = int(math.log2(N))
    return K
try:
    N = int(input("Введите целое число N (>0), являющееся двойки: "))
    K = front(N)
    print(f"K ={K}")
except ValueError:
    print()