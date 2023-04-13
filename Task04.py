# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# Логика решения: Всего журавликов S Петя и Серёжа делают по x журавликов соответственно вместе это 2x,
# а Катя делает 2*2x =4x, s = 6x,  при числе не кратном 6 Катя делает до 4х+3 журавликов,
# допустим что Петя делает журавлика чуть быстрее Серёжи


s = int(input("Введите число S "))
x = s//6
if s % 6 == 0:
    print("Петя и серёжа сделали по", x,
          "журавликов, а Катя сделала", 4 * x, "журавликов")
elif s % 6 < 4:
    print("Петя и серёжа сделали по", x, "журавликов, а Катя сделала",
          4 * x + (s - x*6), "журавликов")
elif s % 6 == 4:
    print("Петя сделал", x + 1, "Серёжа", x, "журавликов, а Катя сделала",
          4 * x + (s - x*6-1), "журавликов")
else:
    print("Петя и серёжа сделали по", x + 1, "журавликов, а Катя сделала",
          4 * x + (s - x*6 - 2), "журавликов")
