#В последовательности на n целых чисел найти и вывести: максимальный среди положительных минимальный среди отрицательных
#произведение элементов
#Составить генератор (yield), который выводит из строки только буквы.

def analyze_sequence(sequence):
    positives = [x for x in sequence if x > 0]
    negatives = [x for x in sequence if x < 0]
    
    max_positive = max(positives) if positives else None
    min_negative = min(negatives) if negatives else None
    
    product = 1
    for num in sequence:
        product *= num
    
    return max_positive, min_negative, product

n = int(input("Введите количество чисел: "))
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(n)]

result = analyze_sequence(numbers)
print(f"Максимальный среди положительных: {result[0]}")
print(f"Минимальный среди отрицательных: {result[1]}")
print(f"Произведение элементов: {result[2]}")


def letter_generator(text):
    for char in text:
        if char.isalpha():
            yield char

text = "Hello World! 123"
gen = letter_generator(text)

print("Буквы из строки:")
for letter in gen:
    print(letter, end=' ')

letters = list(letter_generator(text))
print("\nСписок букв:", letters)