# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input("Введите длину массива: "))

a = [random.randint(1, 10) for _ in range(n)]

x = int(input("Введите число X: "))

closest_num = a[0]
min_diff = abs(x - a[0])

for i in range(1, n):
    diff = abs(x - a[i])
    if diff < min_diff:
        closest_num = a[i]
        min_diff = diff

print("Массив: ", a)
print("Ближайшее число: ", closest_num)
