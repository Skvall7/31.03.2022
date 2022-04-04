list_cub = []
index = 1
result = 0
result_2 = 0
while index < 1000:
    list_cub.append(index ** 3)
    index += 2
for number in list_cub:
    calculation = number % 10000000000 // 1000000000 + number % 1000000000 // 100000000 + number % 100000000 // 10000000 + number % 10000000 // 1000000 + number % 1000000 // 100000 + number % 100000 // 10000 + number % 10000 // 1000 + number % 1000 // 100 + number % 10 + number % 100 // 10
    if calculation % 7 == 0:
        result = result + number
    number_2 = number + 17
    calculation_2 = number_2 % 10000000000 // 1000000000 + number_2 % 1000000000 // 100000000 + number_2 % 100000000 // 10000000 + number_2 % 10000000 // 1000000 + number_2 % 1000000 // 100000 + number_2 % 100000 // 10000 + number_2 % 10000 // 1000 + number_2 % 1000 // 100 + number_2 % 10 + number_2 % 100 // 10
    if calculation_2 % 7 == 0:
        result_2 = result_2 + number_2
print(f'Результат пункта A: {result}')
print(f'Результат пункта B: {result_2}')
