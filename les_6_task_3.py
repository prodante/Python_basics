"""  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров). """

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        Worker.__init__(self, name, surname, position, income)

    def get_full_name(self):
        return self.surname, self.name

    def get_total_income(self):
        return sum(self._income.values())
    
posit = Position('Иван', 'Петров', 'мастер', {'wage': 15000, 'bonus': 5000})
print(f'Сотрудник {posit.get_full_name()}')
print(f'Доход с учетом премии составляет {posit.get_total_income()}')