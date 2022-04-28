with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        with open('dict_users.txt', 'w', encoding='utf-8') as fw:
            user = ' '.join(users.readline().strip('\n').split(','))
            hob = hobby.readline().strip('\n')
            fw.writelines(f'{user} - {hob}\n')
            dictionary = dict.fromkeys([user], hob)
            while True:
                user = ' '.join(users.readline().strip('\n').split(','))
                hob = hobby.readline().strip('\n')
                if not user and hob:
                    print('Код "1"')
                    break
                if not hob:
                    if not user:
                        break
                    key = dict.fromkeys([user])
                    dictionary.update(key)
                    fw.writelines(f'{user} - {None}\n')
                else:
                    dictionary.update({user: hob})
                    fw.writelines(f'{user} - {hob}\n')
print(dictionary)

