list_cub = [149 ** 3, 18 ** 3, 998 ** 3]
print(list_cub)
for number in list_cub:
    calculation = number % 10000000000 // 1000000000 + number % 1000000000 // 100000000 + number % 100000000 // 10000000 + number % 10000000 // 1000000 + number % 1000000 // 100000 + number % 100000 // 10000 + number % 10000 // 1000 + number % 1000 // 100 + number % 10 + number % 100 // 10
    if calculation % 7 == 0:
        text = 'целое число'
    else:
        text = 'не целое число'
    print(f'{calculation} делённое на 7 {text}')
    if (calculation + 17) % 7 == 0:
        text = 'целое число'
    else:
        text = 'не целое число'
    print(f'{calculation} + 17 делённое на 7 {text}')

