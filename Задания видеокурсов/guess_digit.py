import random
print('Загадайте число от 1 до 100, я постараюсь отгадать.')
start, end = 1, 100
input('Нажмите любую клавишу')
while True:
    number = random.randint(start, end)
    print(f'Число {number} я угадал?')
    answer = input('Введите ваш ответ: ')
    if answer == '<':
        end = number
    elif answer == '>':
        start = number
    elif answer == '=':
        print(f'Ура я отгадал! {number} верное число.')
        break
    else:
        print('Я такое не понимаю, если больше ">", если меньше "<", если равно "=". Так я сумею понять.')
