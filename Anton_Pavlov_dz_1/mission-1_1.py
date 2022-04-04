duration = int(input('Введите число в секундах: '))
while duration < 0:
    print('Вводите положительное значение')
    duration = int(input('Введите число в секундах: '))
else:
    sec = duration % 60
    minute = duration // 60 % 60
    hour = duration // 60 // 60 % 24
    days = duration // 60 // 60 // 24 % 30
if duration < 60:
    print(f'{sec} сек')
elif 60 <= duration < 3600:
    print(f'{minute} мин {sec} сек')
elif 3600 <= duration < 86400:
    print(f'{hour} час {minute} мин {sec} сек')
else:
    print(f'{days} день {hour} час {minute} мин {sec} сек')
