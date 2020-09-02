input_list = input("Введите элементы для списка через пробел: ").split()
print(f"Введенный список элементов: {input_list}")
for i in range(1, len(input_list), 2):
    input_list[i - 1], input_list[i] = input_list[i], input_list[i - 1]
print(f"Измененный список элементов: {input_list}")
