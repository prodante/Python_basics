# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(x,y,z):
    l = sorted([x,y,z], reverse=True)
    return sum(l[:-1])

a,b,c = 7,5,10
print(my_func(a,b,c))