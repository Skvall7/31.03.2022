duration = int(input('Введите число в секундах: '))
sec = duration % 60
minute = duration // 60 % 60
hour = duration // 60 // 60 % 24
days = duration // 60 // 60 // 24 % 30
print(f'{days} день {hour} час {minute} мин {sec} сек')
