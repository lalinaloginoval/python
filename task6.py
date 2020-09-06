def int_func(row):
    return row.title()


str_row = input('Введите несколько слов с прописной буквы: ')
print(int_func(str_row))
