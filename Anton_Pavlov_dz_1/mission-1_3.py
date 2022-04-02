number = 1
while number < 101:
    if 20 < number < 100:
        if number % 10 == 1:
            ending = ''
        elif 1 < number % 10 <= 4:
            ending = 'а'
        else:
            ending = 'ов'
    else:
        if number == 1:
            ending = ''
        elif 1 < number <= 4:
            ending = 'а'
        else:
            ending = 'ов'
    print(f'{number} процент{ending}')
    number += 1
