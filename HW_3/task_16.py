# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

n = int(input("Введите количество элементов в массиве: "))
arr = [random.randint(1, 10) for i in range(n)]

x = int(input("Введите искомое число: "))
count = arr.count(x)

print("Сгенерированный массив: ", arr)
print("Количество вхождений числа", x, "в массив: ", count)