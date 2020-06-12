from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('ведіть суму:'))
            break
        except ValueError:
            print("Error")
    while True:
        try:
            p = converter[input('Валюта:')]
            break
        except KeyError:
            print('Error')
    if p == converter.USD:
        x *= 24.58
        print(f'В USD {x}')
    elif p == converter.EUR:
        x *= 26.91
        print(f'В EUR {x}')
    elif p == converter.CZK:
        x *= 1.08
        print(f'В CZK {x}')
    elif p == converter.PLN:
        x *= 6.31
        print(f'В PLN {x}')
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
