# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
str_line = []
while True:
    s = input('Введите данные (построчно) для записи в файл (выход пустая строка)\n')
    if s == '':
        break
    else:
        str_line.append(s)

with open ('les5_task1.txt', 'w', encoding='utf-8') as f_obj:
    for line in str_line:
        f_obj.write(line + '\n')
print(f'Данные записаны в файл {f_obj.name}')

print('Читаем содержимое файла:')
with open ('les5_task1.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
str_line.clear()