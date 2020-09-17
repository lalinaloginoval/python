"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color} {self.name} начал движение!'

    def stop(self):
        return f'{self.color} {self.name} остановился!'

    def turn(self, direction):
        return f'{self.color} {self.name} повернул {direction}!'

    def show_speed(self):
        return f'{self.color} {self.name} едет со скоростью {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        return f'{self.color} {self.name} превысил скорость на {self.speed - 60} км/ч.' if (self.speed > 60) else \
            Car.show_speed(self)


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        return f'{self.color} {self.name} превысил скорость на {self.speed - 40} км/ч.' if (self.speed > 40) else \
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print(f'Это полицеский {self.color} {self.name}.')


sport_auto = SportCar(120, 'Красный', 'Порше', False)
print(sport_auto.turn('налево'))
print(sport_auto.show_speed())

town_auto = TownCar(70, 'Черный', 'Мерседес', False)
print(town_auto.go())
print(town_auto.show_speed())

police_auto = PoliceCar(100, 'Белый', 'Ауди')
print(police_auto.go())
print(f'{police_auto.name} преследует {sport_auto.color} {sport_auto.name}')

work_car = WorkCar(41, 'Синий', 'БМВ', False)
print(work_car.turn('направо'))
print(work_car.stop())
