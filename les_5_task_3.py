# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
from functools import reduce

def read_file():
    s = []
    print('Читаем содержимое файла:')
    with open ('les5_task3.txt', encoding='utf-8') as f_obj:
        for line in f_obj:
            print(line.replace('\n', ''))
            for var_l in line.split():
                s.append(var_l)
    return s

def oklad(arr):
    return [arr[i-1] for i in range(1, len(arr), 2) if int(arr[i]) < 20000]

def number(x):
    if x.isdigit():
        return 1
    else:
        return 0

sotr = read_file()
print(f'Сотрудники с окладом менее 20 тыс.: {oklad(sotr)}')

# 1) Cредняя величина дохода сотрудников (sum, map, filter)
oklad_s = sum(list(map(int, filter(number, sotr))))/len(list(filter(number, sotr)))
print(f'Cредняя величина дохода сотрудников {oklad_s:.3f}')

# 2) Cредняя величина дохода сотрудников (reduce)
#print(f'Cредняя величина дохода сотрудников {reduce((lambda x,y: x + y), [int(sotr[i]) for i in range(1, len(sotr), 2)])/(len(sotr)/2):.3f}')


