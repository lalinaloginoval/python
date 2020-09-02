number = int(input("Введите количество уникальных товаров для аналитки: "))
product_list = []
i = 1
while i <= number:
    name = input("Название: ")
    price = int(input("Цена: "))
    count_pr = int(input("Количество: "))
    ed = input("Ед: ")
    character = {"название": name, "цена": price, "количество": count_pr, "ед": ed}
    product_list.append(tuple([i, character]))
    i = i + 1
print(product_list)

product_dict = {}
for product in product_list:
    for key, value in product[1].items():
        product_dict.setdefault(key, []).append(value)
print(product_dict)
