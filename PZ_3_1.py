a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
positive = sum([a > 0, b > 0, c > 0])
if positive == 1:
    print("Истино: Ровно одно из чисел a, b, c положительно.")
else:
    print("Ложно: Не ровно одно из  чисел a, b, c положительно.")