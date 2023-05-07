# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def arithmetic_progression(a, n, d):
    arith_list = []
    num = a
    for i in range(n):
        arith_list.append(num)
        num += d
    return arith_list


first_elem = int(input("Введите a="))
diff = int(input("Введите разность d="))
number = int(input("Введите колличество эл-в n="))
list = arithmetic_progression(first_elem, number, diff)
d1 = int(input("Введите начало диапазона "))
d2 = int(input("Введите конец диапазона "))
print(list)
for i in range(len(list)):
    if d1 <= list[i] <= d2:
        print(i, end=(' '))

