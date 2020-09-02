input_number = int(input("Введите оценку для составления рейтинга: "))
rating_list = [7, 5, 3, 3, 2, input_number]
print(sorted(rating_list, reverse=True))
