# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def Step(a,b):
    if b == 0:
        return 1
    if b < 0:
        return Step(a, b+1) * 1 / a
    return Step(a, b - 1) * a

a, b = int(input()), int(input())
print(Step(a,b))

