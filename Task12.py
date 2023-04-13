# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.

# для решения задачи нам надо решить 2 уровнения: х+у=S и х*у=P для этого надо решить квадратное уравнение
# -x^2 + Sx - P=0  a=-1 b=S c=-p

# математическое решение

import math

s = int(input("S= "))
p = int(input("P="))
a = -1
b = s
c = -p
dis = b * b - 4 * a * c
if dis > 0:
    x1 = int((-b + math.sqrt(dis)) // 2 * a)
    x2 = int((-b - math.sqrt(dis)) // 2* a)
    print("загаданные числа равны", x1, x2)
elif dis == 0:
    x1 =int(-b / 2 * a)
    print("загадано одинаковое число",x1)
else:
    print("при данных исходных решений нет")


# решение перебором
s1 = int(input("S= "))
p1 = int(input("P="))

for i in range(1001):
    if i * (s1 - i) == p1:
        print("Загаданные числа ->", i, s1-i)
        break
else:
    print("при данных исходных решений нет")