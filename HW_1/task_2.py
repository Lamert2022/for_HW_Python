# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


print("Введите трёхзначное число:")
number = input()
print("Сумма цифр трехзначного числа равна: ", sum([int(number[0]), int(number[1]), int(number[2])]))
