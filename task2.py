"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ExceptionZero(Exception):
    def __init__(self, text):
        self.text = text


division = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))
try:
    if divisor == 0:
        raise ExceptionZero("Вы ввели в делителе 0!")
except ExceptionZero as err:
    print(err.text)
else:
    print(f'Частное = {division / divisor}')