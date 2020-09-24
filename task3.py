"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExceptionList(Exception):
    def __init__(self, text):
        self.text = text


print('Введите данные для списка или "q" для завершения: ')
total_list = []
while True:
    input_ = input()
    if input_ not in ['q', 'Q']:
        try:
            if input_.isdigit():
                total_list.append(input_)
            else:
                raise ExceptionList(f'Введена строка!')
        except ExceptionList as err:
            print(err.text)
    else:
        break

print(f'Полученный список: {total_list}')
