namber = int(input("Введите трехзначное число: "))
a = namber % 10
b = (namber // 10) % 10
print(f"Последняя цифра: {a} ")
print(f"Средняя цифра: {b} ")