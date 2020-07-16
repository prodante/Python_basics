# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce

# ********************************* плохой вариант ******************************* #
my_list = [i for i in range(0, 10)]
print(f'Набор чисел для записи в файл: {my_list}')
with open ('les5_task5.txt', 'w', encoding='utf-8') as f_obj:
    for line in my_list:
        f_obj.write(str(line) + ' ')
print(f'Данные записаны в файл {f_obj.name}')

with open ('les5_task5.txt', encoding='utf-8') as f_obj:
    for num in f_obj:
        sum_ = list(num.replace(' ',''))

print(f'Cумму чисел в файле равна {reduce((lambda x,y: x+y), [int(sum_[i]) for i in range(0, len(sum_))])}')

# ********************************* хороший вариант ******************************* #
# def summary():
#     try:
#         with open('les5_task5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()

#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()