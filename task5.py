def sum_numbers():
    sum_result = 0
    exit_ = False

    while not exit_:
        numbers = input('Введите числа через пробел или нажмите Q для выхода: ').split()

        result = 0
        for ind in range(len(numbers)):
            if numbers[ind] in ['q', 'Q']:
                exit_ = True
                break
            else:
                result += int(numbers[ind])
        sum_result += result
        print(f'Текущая сумма чисел: {sum_result}')
    print(f'Итоговая сумма чисел: {sum_result}')


sum_numbers()
