from sys import argv

file_name, time, salary, bonus = argv

time = int(time)
salary = int(salary)
bonus = int(bonus)
print(f'Заработная плата сотрудника - {time * salary + bonus}')

# python task1.py 20 1000 33000
