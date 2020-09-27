"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. 5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from collections import defaultdict


class Stock:
    stock_full = defaultdict(list)

    @staticmethod
    def reception_stock(department, device_dep):
        Stock.stock_full[department].append(device_dep)


class OfficeEquipment:
    def __init__(self, device, name, quantity):
        self.device = device
        self.name = name
        self.quantity = quantity
        self.device_dep = {}

    def reception(self, device_add, department):
        if self.validate:
            self.device_dep.update(device_add)
            Stock.reception_stock(department, self.device_dep)
            print(f'Добавлен {self.device} {self.name} в количестве {self.quantity} шт.')
        else:
            print(f'{self.device} не добавлен!')

    @property
    def validate(self):
        try:
            int(self.quantity)
            return True
        except ValueError:
            return False


class Printer(OfficeEquipment):
    device = 'принтер'

    def __init__(self, name, quantity, volume):
        super().__init__(self.device, name, quantity)
        self.volume = volume

    def reception(self, department, device_add=None):
        device_add = {self.device: {'модель': self.name, 'количество': self.quantity, 'объем картриджа': self.volume}}
        super().reception(device_add, department)


class Scanner(OfficeEquipment):
    device = 'сканер'

    def __init__(self, name, quantity, qr_code):
        super().__init__(self.device, name, quantity)
        self.qr_code = qr_code

    def reception(self, department, device_add=None):
        device_add = {self.device: {'модель': self.name, 'количество': self.quantity, 'QR-код': self.qr_code}}
        super().reception(device_add, department)


class Copier(OfficeEquipment):
    device = 'ксерокс'

    def __init__(self, name, quantity, is_color):
        super().__init__(self.device, name, quantity)
        self.is_color = is_color

    def reception(self, department, device_add=None):
        device_add = {self.device: {'модель': self.name, 'количество': self.quantity, 'цветной': self.is_color}}
        super().reception(device_add, department)


printer = Printer('HP', 1, 10)
printer.reception('Веб-отдел')

copier = Copier('Xerox', 2, 'да')
copier.reception('Веб-отдел')

scanner = Scanner('Sony', 5, 'поддерживается')
scanner.reception('Сервис')
print(f'На складе: {dict(Stock.stock_full)}')
