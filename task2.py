"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    # Преобразуем метод в свойство
    @property
    def calc_tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def calc_tissue_consumption(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat(42)
print(f'Расход ткани на пальто размера {coat.size} составит {coat.calc_tissue_consumption} м.')
suit = Suit(170)
print(f'Расход ткани на костюм на рост {suit.height} составит {suit.calc_tissue_consumption()}')
