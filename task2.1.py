from datetime import datetime, timedelta


def get_time():
    sec = timedelta(seconds=int(input('Введите время в секундах: ')))
    d = datetime(1, 1, 1) + sec
    print(f'{d.hour}:{d.minute}:{d.second}')


get_time()
