input_str = input("Введите несколько слов: ").split()
for ind, el in enumerate(input_str):
    print(ind, el[:10])
