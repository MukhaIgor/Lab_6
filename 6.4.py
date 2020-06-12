while True:
    while True:
        try:
            t = int(input('Ввеіть хвилину:'))
            break
        except ValueError:
            print('Введіть хвилину')
    while t < 0 or t > 60:
        t = int(input('Введіть хвилину!'))
    svetofor = t % 6
    if 0 <= svetofor < 3:
        print('Зелений')
    elif 3 <= svetofor <= 4:
        print('Жовтий')
    else:
        print('Червоний')
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
