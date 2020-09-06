def del_func(arg1, arg2):
    if arg2 == 0:
        print('Делить на 0 нельзя!')
        return
    return print(f'{arg1} / {arg2} = {arg1 / arg2}')


dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))
del_func(dividend, divisor)
