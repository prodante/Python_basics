""" Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра. """

# описывае класс-родитель Stationery (канцелярская принадлежность)
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('“Запуск отрисовки {self.title}.”')

#*************************** cоздание дочерних классов ***************************#
# класс ручка 
class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'“Запуск отрисовки {self.title}.”')

# класс карандаш
class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'“Запуск отрисовки {self.title}.”')  

# класс маркер 
class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f'“Запуск отрисовки {self.title}.”')

# основная фнкция
def main():
    pen = Pen('ручка')
    pencil = Pencil('карандаш')
    handle = Handle('маркер')
    pen.draw()
    pencil.draw()
    handle.draw()

main()