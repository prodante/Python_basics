# coding=utf8
""" Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. """
import time
from itertools import cycle

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        i, counter = 0, 0
        for el in cycle(self.__color):
            if counter == 11:
                break
            if i == 0:
                time.sleep(7)
                s_color = '\033[31m'
                i = 1
            elif i == 1:
                time.sleep(2)
                s_color = '\033[33m'
                i = 2
            elif i == 2: 
                time.sleep(7)
                s_color = '\033[32m'
                i = 3
            else:
                time.sleep(2)
                s_color = '\033[33m'
                i = 0   
            print(f'{s_color} {el}')
            counter += 1
        print('\033[37m')

color_traff = ('red', 'yellow', 'green', 'yellow')
tr = TrafficLight(color_traff)
tr.running()