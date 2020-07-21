""" Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат. """
from random import choice

# описывае класс-родитель Car
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, скорость {self.speed} км/ч')
    
    def go(self): 
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} поехала {direction}')
    
    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км/ч'

#*************************** cоздание дочерних классов ***************************#
# класс TownCar 
class TownCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км/ч' if self.speed <= 60 else f'Автомобиль {self.name} перевысил скорость на {self.speed - 60} км/ч'

# класс WorkCar 
class WorkCar(Car):

    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км/ч' if self.speed <= 40 else f'Автомобиль {self.name} перевысил скорость на {self.speed - 40} км/ч'

# класс SportCar 
class SportCar(Car):

    def show_(self):
        print(f'Вау, какая {self.color} малышка!')

# класс PoliceCar
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        Car.__init__(self, speed, color, name, is_police)

    def show_(self):
        print(f'Опа впреди копы, на {self.name}')

# основная фнкция
def main():
    direction = ['вперед', 'назад', 'влево', 'вправо', 'а нет развернулся']
    #***************************************************************#
    city_car = TownCar(80, 'красный', 'TOYOTA CAMRI')
    city_car.show()
    city_car.stop()
    city_car.go()
    city_car.turn(choice(direction))
    print(city_car.show_speed())
    #***************************************************************#
    print('*'*100)
    w_car = WorkCar(60, 'серый', 'ГАЗ')
    w_car.show()
    w_car.stop()
    w_car.go()
    w_car.turn(choice(direction))
    print(w_car.show_speed())
    #***************************************************************#
    print('*'*100)
    s_car = SportCar(120, 'Гейзер', 'Lamborghini Diablo')
    s_car.show_()
    s_car.show() 
    #***************************************************************#
    print('*'*100)
    cop_car = PoliceCar(60, 'Валентина', 'Corvette')
    cop_car.show_()
    cop_car.show()

main()





