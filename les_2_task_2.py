# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
l = input('Введите элементы списка через пробел: ')
l = l.split() # делаем список
# l = [1, 'Hi', (1,2), 4, 5, 6, 7]
print(f'Исходный список: {l}')
for id_ in range(len(l)):
    if id_ % 2 == 0 and id_ < len(l)-1:
        l[id_], l[id_+1] = l[id_+1], l[id_]
print(f'{" "*6}Результат: {l}')