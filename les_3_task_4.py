# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func(x,y):
    # try:
    #     return int(x)**int(y)
    # except ValueError:
    #     return 'Символ там, где ожидается число'
    span = x
    for _ in range(1,abs(y)):
        x = x * span
    if y == 0:
        return 1
    elif y > 0:  
        return x
    else:
        return 1/x

try:
    number = int(input('Введите действительное положительное число: '))
    power = int(input('Введите целое отицательное число: '))
except ValueError:
    print('Символ там, где ожидается число')
except ZeroDivisionError:
    print('Ошибка деления на нуль')
else:
    print(f'Число {number}^{power} = {my_func(number,power):.10f}')