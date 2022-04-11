import random

start, end = 1, 100
print('Загадайте число от 1 до 100, я постараюсь отгадать.')
input('Нажмите любую клавишу')
while True:
    number = random.randint(start, end)
    print(f'Число {number} я угадал?')
    answer = input('Введите ваш ответ: ')
    if answer == '<':
        end = number - 1
    elif answer == '>':
        start = number + 1
    elif answer == '=':
        print(f'Ура я отгадал! {number} верное число.')
        break
    else:
        print('Я такое не понимаю, если больше ">", если меньше "<", если равно "=". Так я сумею понять.')
    if start == end:
        print(f'Других вариантов то нет, {number} ваше число!')
        break
    if end == number or start == number:
        print('Так не может быть, начнем с начала')
        start, end = 1, 100

