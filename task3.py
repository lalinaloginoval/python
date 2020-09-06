def sum_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.sort(reverse=True)
    return print(f'{my_list[0]} + {my_list[1]} = {my_list[0] + my_list[1]}')


number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
sum_func(number1, number2, number3)
