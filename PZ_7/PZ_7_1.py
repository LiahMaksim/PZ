#Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.

def count_lowercase_letters(text):
    count = 0
    for char in text:
        if 'a' <= char <= 'z':
            count += 1
        elif 'а' <= char <= 'я':
            count += 1
    return count
print("Вывод")
test_strings = [
    "Hello World! Привет Мир!",
    "abcABCабвАБВ",
    "123!@# test тест",
    "Только русские буквы",
    "only english letters"
]
for test in test_strings:
    result = count_lowercase_letters(test)
    print(f"Строка: '{test}'")
    print(f"Количество строчных букв: {result}\n")