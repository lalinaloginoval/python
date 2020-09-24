"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
from datetime import datetime


class Date:
    def __init__(self, date_str):
        self.date_str = str(date_str)

    @classmethod
    def parser_int_date(cls, date_str):
        date_int = [int(el) for el in date_str.split('-')]
        return date_int

    @staticmethod
    def validate(day, month, year):
        try:
            if datetime(year, month, day):
                print('Дата корректна!')
        except ValueError:
            print('Введенная дата некорректна!')


date = Date.parser_int_date('30-01-2020')
print(f'{date[0]}.{date[1]}.{date[2]}')
Date.validate(date[0], date[1], date[2])

date = Date.parser_int_date('30-02-2020')
print(f'{date[0]}.{date[1]}.{date[2]}')
Date.validate(date[0], date[1], date[2])