number = int(input('Введите число: '))
number2 = int(str(f'{number}{number}'))
number3 = int(str(f'{number}{number}{number}'))

print(f"{number} + {number2} + {number3} = {number + number2 + number3}")
