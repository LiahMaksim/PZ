#Дан целочисленный список размера N, все элементы которого упорядочены (по 
# возрастанию или по убыванию). Найти количество различных элементов в данном списке.

def front(sorted_list):
    return len(set(sorted_list))

sorted_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(front(sorted_list))