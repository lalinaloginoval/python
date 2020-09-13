"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator
translator = Translator()
new_file = []

try:
    with open('file_task4.txt', 'r', encoding='utf-8') as my_file:
        for line in my_file:
            line = line.split(' ', 1)
            word = translator.translate(line[0], dest='ru')
            new_file.append(word.text + ' ' + line[1])
        print(new_file)
except IOError:
    print('Произошла ошибка ввода-вывода')

try:
    with open('file_task4_new.txt', 'w') as file_new:
        file_new.writelines(new_file)
except IOError:
    print('Произошла ошибка ввода-вывода')