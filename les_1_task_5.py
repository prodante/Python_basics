# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Введите выручку фирмы: "))
expenses = int(input("Введите издержки фирмы: "))
if revenue > expenses:
    efficiency = revenue / expenses
    print('Соласно финансовым показателям деятельность фирмы прибыльна!', end=' ')
    print(f'Рентабельность фирмы {efficiency:.2f}')
    num_empl = int(input('Введите численность сотрудников фирмы: '))
    efficiency_empl = revenue / num_empl
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет {efficiency_empl:.2f}')
elif revenue == expenses:
    print('Соласно финансовым показателям рентабельность фирмы равна нулю!')
else:
    print('Соласно финансовым показателям деятельность фирмы убыточна!')