def thesaurus(names):
    dict_names = {}
    for name in names:
        title = name[0]
        if title in dict_names:
            dict_names[title] = dict_names[title] + [name]
        dict_names.setdefault(title, [name])
    print(dict_names)


list_names = ["Иван", "Мария", "Петр", "Илья", "Паша"]

thesaurus(list_names)
