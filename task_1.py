"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        # Возвращает бесконечный цикл переключения светофора, выход осуществляется путем остановки программы
        while True:
            i = 0
            while i < len(TrafficLight.__color):
                color_text = '\033[31m' if i == 0 else \
                    '\033[32m' if i == 2 else '\033[33m'

                print(f'{color_text} {TrafficLight.__color[i]}')
                sleep(7) if i in (0, 2) else sleep(2)

                i += 1


trafficLight = TrafficLight()
trafficLight.running()