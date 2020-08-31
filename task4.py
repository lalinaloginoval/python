number = int(input("Введите целое положительное число: "))
list_number = []

while number > 0:
    list_number.append(number % 10)
    number //= 10

max_number = max(list_number)
print(max_number)

# list_number = list(map(int, number))
