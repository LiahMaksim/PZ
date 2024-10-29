import math
def find_exponent(N):
    if N <= 0 or (N & (N - 1)) != 0:
        raise ValueError("N должно быть положительным и являться степенью двойки.")
    K = int(math.log2(N))
    return K
try:
    N = int(input("Введите целое число N (>0), являющееся двойки: "))
    K = find_exponent(N)
    print(f"K ={K}")
except ValueError as e:
    print(e)