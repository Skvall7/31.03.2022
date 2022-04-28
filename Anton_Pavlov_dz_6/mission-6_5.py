def list_join(argv):
    def fio(user_fio: list):
        """Принимает список, возвращает словарь. Фамилия имя отчество"""
        return {'фамилия': user_fio[0], 'имя': user_fio[1], 'отчество': user_fio[2]}

    with open(argv[1], encoding='utf-8') as users:
        with open(argv[2], encoding='utf-8') as hobby:
            with open(argv[3], 'w', encoding='utf-8') as fw:
                user = users.readline().strip('\n').split(',')
                hob = set(hobby.readline().strip('\n').split(','))
                fw.writelines(f'{user} - {hob}\n')
                dictionary = {' '.join(fio(user).values()): hob}
                while True:
                    user = users.readline().strip('\n').split(',')
                    hob = set(hobby.readline().strip('\n').split(','))
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


if __name__ == '__main__':
    import sys
    exit(list_join(sys.argv))
