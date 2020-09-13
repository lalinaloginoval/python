"""
 Создать программно файл в текстовом формате,
 записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
exit_ = False

with open("file_task1.txt", "w", encoding="utf-8") as my_file:
    print('Введите данные для записи: ')
    while not exit_:
        input_str = input()
        if input_str == "":
            exit_ = True
            break
        else:
            my_file.write(input_str + '\n')
