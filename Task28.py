# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum_number(a, b):
    if b == 0:
        return a
    return sum_number(a + 1, b - 1)


x = input('Введите числа через пробел ').split()
print(sum_number(int(x[0]), int(x[1])))
