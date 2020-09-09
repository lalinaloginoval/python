from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


n = int(input('Введите число для вычисления факториала: '))
for el in fact(n):
    print(el)
