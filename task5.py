from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


my_list = [el for el in range(100, 1001, 2)]
print('Результат перемножения всех элементов списка:', reduce(my_func, my_list))
