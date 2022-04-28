def thesaurus_adv(names):
    dict_names = {}
    for name in names:
        second_name = name.split(' ')[-1]
        first_name = name.split(' ')[0]
        tittle_s = second_name[0]
        tittle_f = first_name[0]
        if tittle_s not in dict_names:
            dict_names[tittle_s] = {tittle_f: [name]}
        else:
            if tittle_f in dict_names[tittle_s]:
                dict_names[tittle_s][tittle_f] = dict_names[tittle_s][tittle_f] + [name]
            else:
                dict_names[tittle_s][tittle_f] = [name]
    print(dict(sorted(dict_names.items())))


list_if = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

thesaurus_adv(list_if)
