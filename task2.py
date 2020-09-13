"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
# Берется текстовый файл из первой задачи

try:
    with open("file_task1.txt", "r", encoding="utf-8") as my_file:
        content = my_file.read().splitlines()
        count_lines = len(content)

        count_words = 0
        num_line = 0
        for line in content:
            count_words = len(line.split())
            num_line += 1
            print(f'Количетсво слов в {num_line}-й строке: {count_words}')

    print(f'Количетсво строк в файле: {count_lines}')
except IOError:
    print('Произошла ошибка ввода-вывода')