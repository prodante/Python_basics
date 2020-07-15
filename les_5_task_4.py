""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """
lang  = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
new_file = []
with open ('les5_task4_en.txt', 'r', encoding='utf-8') as f_obj_en:
    for line in f_obj_en:
        line = line.split(' ', 1)
        new_file.append(lang[line[0]] + ' ' + line[1])

with open('les5_task4_ru.txt', 'w', encoding='utf-8') as f_obj_ru:
    f_obj_ru.writelines(new_file)