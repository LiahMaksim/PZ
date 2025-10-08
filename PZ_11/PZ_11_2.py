#Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое, количество букв в нижнем регистре. 
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open('text18-15.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
lower_count = sum(c.islower() for line in text for c in line)
print("Содержимое файла:")
print(''.join(text))
print(f'Количество букв в нижнем регистре: {lower_count}')
with open('result15_2.txt', 'w', encoding='utf-8') as f:
    f.writelines([line.upper() for line in text])