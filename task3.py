"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

try:
    with open("file_task3.txt", "r", encoding="utf-8") as my_file:
        salary = []
        employee = []
        lines = my_file.read().splitlines()
        for line in lines:
            line = line.split()
            if float(line[1]) < 20000:
                employee.append(line[0])
            salary.append(line[1])

    print(f'Сотрудники с окладом меньше 20 тыс.: {employee}, средний оклад - {sum(map(float, salary)) / len(salary)}')
except IOError:
    print('Произошла ошибка ввода-вывода')