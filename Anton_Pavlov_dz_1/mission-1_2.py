list_cub = []
index = 1
result = 0
result_2 = 0
summa = 0
while index < 1000:
    list_cub.append(index ** 3)
    index += 2
for number in list_cub:
    calculation = 0
    calculation_2 = 0
    summa = number
    number_2 = number + 17
    summa_2 = number_2
    while number > 0:
        calculation += number % 10
        number //= 10
    if calculation % 7 == 0:
        result += summa
    while number_2 > 0:
        calculation_2 += number_2 % 10
        number_2 //= 10
    if calculation_2 % 7 == 0:
        result_2 += summa_2
print(f'Результат пункта A: {result}')
print(f'Результат пункта B: {result_2}')
