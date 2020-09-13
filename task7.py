"""
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""
import json

profit = {}
count_firm = 0
prof = 0
with open('file_task7.txt', 'r', encoding='utf-8') as file:
    for context in file:
        name, type_firm, earning, damage = context.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            count_firm += 1
    if count_firm != 0:
        prof_aver = prof / count_firm
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit_list = [profit, pr]
    print(f'Прибыль каждой компании - {profit_list}')

with open('file_task7.json', 'w', encoding='utf-8') as file_js:
    json.dump(profit_list, file_js, indent=4, ensure_ascii=False)

    js_str = json.dumps(profit_list, indent=4, ensure_ascii=False)
    print(f'Создан файл с расширением json: \n {js_str}')