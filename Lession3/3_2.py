# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

x = int(input('Число, колличество которого нужно найти: '))
n = list(map(int,input().split()))

# for i in range(1, len(n)):
#     if n[i] == x:
#         print(n[i-1])
#         break
#     elif n[i] > x and n[i-1] < x:
#         print(n[i-1])
#         break
for i in range(1, len(n)):
    if n[i] >= x:
        print(n[i-1])
        break
