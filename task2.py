def person_info(name, last_name, year_bd, city, email, phone):
    print(f'Данные пользователя: {name} {last_name}, {year_bd} г.р., г.{city}, e-mail:{email}, тел:{phone}')


person_info(name='Иван', last_name='Иванов', year_bd=1990,
            city='Москва', email='ivan_ivanov@email.ru', phone='+79099090099')
