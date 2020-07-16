# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
kol = 0
print('Читаем содержимое файла:')
with open ('les5_task2.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        str_kol = len(line.split())
        print(line.replace('\n', ''), end='  -  ')
        print('кол-во слов', len(line.split(' ')))
        kol += 1
print(f'Количество строк {kol}')