# coding=utf8
""" Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}] """

import json
result = []
with open('les5_task7.json', 'w', encoding='utf-8') as fw_obj:
    with open('les5_task7.txt', encoding='utf-8') as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        ave_profit = sum([int(i) for i in profit.values() if int(i) > 0])/len([int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'ave_profit': round(ave_profit)})
    json.dump(result, fw_obj)

# import re

# def number(x):
#     if x.isdigit():
#         return 1
#     else:
#         return 0

# li = []
# result = []
# with open ('les5_task7.txt', encoding='utf-8') as f_obj:
#     x = f_obj.readlines()
# for i in x:
#     #print(re.split(r'[\\(\)\:\n\.\-\']', i)) 
#     li.append(re.split(r'\W+', i))
# print(li)
# for i in li:
#     result.append(list(map(int, filter(number, i))))
# print(result)
