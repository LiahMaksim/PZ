#. Дан список размера N. Осуществить циклический сдвиг элементов списка влево на 
# одну позицию (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN).

def cyclic_shift_left(A):
    if len(A) == 0:
        return A
    return A[1:] + [A[0]]

A = [1, 2, 3, 4, 5, 6, 7, 8]
print(cyclic_shift_left(A))