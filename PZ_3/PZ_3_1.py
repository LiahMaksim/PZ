#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    front = sum([a > 0, b > 0, c > 0])
    if front == 1:
        print("Истино: Ровно одно из чисел a, b, c положительно.")
    else:
        print("Ложно: Не ровно одно из  чисел a, b, c положительно.")
except ValueError:
    print("Ошибка: Пожалуйста, введите корректные числовые значения.")
