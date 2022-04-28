def fio(user_fio: list):
    """Принимает список, возвращает словарь. Фамилия имя отчество"""
    return {'фамилия': user_fio[0], 'имя': user_fio[1], 'отчество': user_fio[2]}


with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        with open('dict_users.txt', 'w', encoding='utf-8') as fw:
            user = users.readline().strip().split(',')
            hob = set(hobby.readline().strip().split(','))
            fw.writelines(f'{user} - {hob}\n')
            dictionary = {' '.join(fio(user).values()): hob}
            while True:
                user = users.readline().strip().split(',')
                hob = set(hobby.readline().strip().split(','))
                if not ''.join(user) and ''.join(hob):
                    print('Код "1"')
                    break
                elif not ''.join(hob):
                    if not ''.join(user):
                        break
                    key = dict.fromkeys([' '.join(fio(user).values())])
                    dictionary.update(key)
                    fw.writelines(f'{user} - {None}\n')
                else:
                    dictionary.update({' '.join(fio(user).values()): hob})
                    fw.writelines(f'{user} - {hob}\n')
# Словарь для фио что бы можно было обратится к любому из значений, множества для хобби т.к. не могут повторятся
print(dictionary)
