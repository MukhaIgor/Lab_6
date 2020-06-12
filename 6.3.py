from enum import Enum


class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


while True:
    while True:
        try:
            s = int(input("month: "))
            break
        except ValueError:
            print('Error')
    if s in range(1, 3) or s == 12:
        print('Winter')
    elif s in range(3, 7):
        print("Spring")
    elif s in range(6, 9):
        print('Summer')
    elif s in range(9, 13):
        print('Autumn')
    else:
        print('Такого місяця не існує')
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
