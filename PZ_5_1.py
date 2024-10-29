def print_custom_string():
    try:
        fan = int(input("Введите количество символов: "))
        if fan <= 0:
            print("Количество символов должно быть положительным. ")
            return
        result_string = '*' * fan
        print(result_string)
    except ValueError:
        print("Пожалуйста, введите целое число.")
print_custom_string()