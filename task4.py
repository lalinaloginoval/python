def elevate_func(x, y):
    return x ** y


def elevate_2_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


input_x = float(input('Введите действительно положительное число: '))
input_y = int(input('Введите целое отрицательное число: '))
print(elevate_func(input_x, input_y))
print(elevate_2_func(input_x, input_y))
