# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n, num1, num2 = int(input("Длина списка: ")), int(input("Минимальное число: ")), int(input("Максимальное число: "))
list_a = []
list_num = [randint(-10, 10) for _ in range(n)]
print(list_num)
for i in range(len(list_num)):
    if num1 <= list_num[i] <= num2:
        list_a.append(i)
print(list_a)
