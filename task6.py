"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""


def replace_f(word):
    # Заменяет конкретные символы на 0 или пустое значение
    return word.replace('-', '0').replace('(пр)', '').replace('(лаб)', '').replace('(л)', '').replace(':', '')


subj = {}
try:
    with open('file_task6.txt', 'r', encoding='utf-8') as init_file:
        for content in init_file:
            subject, lecture, practice, lab = content.split()
            subj[replace_f(subject)] = int(replace_f(lecture)) + int(replace_f(practice)) + int(replace_f(lab))
        print(f'Общее количество часов по предметам - {subj}')
except IOError:
    print('Произошла ошибка ввода-вывода')