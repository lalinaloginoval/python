"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

try:
    with open('file_task5.txt', 'w+', encoding='utf-8') as my_file:
        numbers = [randint(0, 1001) for el in range(10)]
        for number in numbers:
            my_file.write(str(number) + ' ')

        my_file.seek(0)
        file_numbers = my_file.read().split()

        sum_numbers = 0
        for file_number in file_numbers:
            sum_numbers += int(file_number)
        print(file_numbers)
        print(f'Сумма чисел в файле: {sum_numbers}')
except IOError:
    print('Произошла ошибка ввода-вывода')