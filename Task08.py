# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# Логика решения: так отломить можно только если k будет кратна n и m

n = int(input("Введите n "))
m = int(input("Введите m "))
k = int(input("Введите k "))
if 1 < k < m * n and (k % m == 0 or k % n == 0):
    print("yes")
elif k == 1 and (m == 1 or n == 1):
    print("yes")
else:
    print("no")
