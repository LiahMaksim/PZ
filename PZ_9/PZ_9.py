 #Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
 #удалить из него первый и последний элементы. Отобразить исходный и получившийся словарь. Использовать for, range.

original_dict = {i: i**3 for i in range(7)}

modified_dict = {}
for key in range(1, len(original_dict) - 1):
    modified_dict[key] = original_dict[key]

print("Исходный словарь:", original_dict)
print("Измененный словарь:", modified_dict)