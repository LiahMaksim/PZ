#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:


with open('numbers.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
count = len(numbers)
min_value = min(numbers)
last_min_index = len(numbers) - 1 - numbers[::-1].index(min_value)
first = numbers[0]
multiplied = [num * first for num in numbers]
with open('result15_1.txt', 'w') as f:
    f.write('Исходные данные:\n')
    f.write(' '.join(map(str, numbers)) + '\n')
    f.write(f'Количество элементов: {count}\n')
    f.write(f'Индекс последнего минимального элемента: {last_min_index}\n')
    f.write('Умножаем все элементы на первый элемент:\n')
    f.write(' '.join(map(str, multiplied)) + '\n')