# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

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
print(list)