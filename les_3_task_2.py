# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def fio(lastname, name, year_date, city, e_mail, tel):
    print(f'{lastname} {name} {year_date} года рождения город {city}. Email: {e_mail}. Телефон: {tel}')

fio(name = input('Введите имя: '), lastname = input('Введите фамилию: '), year_date = input('Введите год рождения: '), city = input('Введите город проживания: '), e_mail = input('Введите email: '), tel = input('Введите телефон: '))