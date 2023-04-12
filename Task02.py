# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Коментарий по решению: данную задачу можно решить двумя способами:
# 1-й через строку 
# 2-й математически

# 1-й способ

n = str(input("Введите число "))  
sum = 0
sum = int(n[0]) + int(n[1]) + int(n[2]) 
print(sum)

# 2-й способ без цикла

number = int(input("Введите трёхзначное число ")) 
if 100 <= number <= 999:
    sum = number % 10
    number = number // 10
    sum += number % 10
    number = number // 10
    sum += number
    print(sum)
else:
    print("Введено не трёхзначное число")

# с циклом
number = int(input("Введите трёхзначное число ")) 
if 100 <= number <= 999:
    sum = 0
    for i in range(3):
        sum += number % 10
        number = number // 10
    print(sum)
else:
    print("Введено не трёхзначное число")
