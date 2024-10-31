#Дан прямоугольник, длины сторон которого равны натуральным числам А и В. Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей площади.

def cut_rectangle_into_squares(A, B):
    if not (isinstance(A, int) and isinstance(B, int)) or A <= 0 or B <= 0:
        raise ValueError("Длины сторон A и B должны быть натуральными числами (положительными числами).")
    count = 0
    while A > 0 and B > 0:
        if A > B:
            count += A // B
            A = A % B
        else:
            count += B // A
            B = B % A
    return count
try:
    A = int(input("Ввежите длину стороны A (натуральное число): "))
    B = int(input("Введите длину стороны B (натуральное число): "))
    result = cut_rectangle_into_squares(A, B)
    print(f"Количество квадратов, на которое можно разрезать прямоугольник: {result}")
except ValueError as e:
    print(e)