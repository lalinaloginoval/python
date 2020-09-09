from itertools import count, cycle

# a)
start_number = int(input('Введите стартовое число: '))
end_number = int(input('Введите конечное число: '))

for el in count(start_number):
    if el > end_number:
        break
    else:
        print(el)

# b)
start_list = input('Введите символы для списка: ')
i = 0
for el in cycle(start_list):
    if i > 10:
        break
    print(el)
    i += 1
