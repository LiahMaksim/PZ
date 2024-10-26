def front(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0:
        return 2
    elif y == 0:
        return 1
    else:
        return 3
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
result = front(x, y)
print(result)