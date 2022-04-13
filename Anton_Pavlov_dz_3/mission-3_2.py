def num_translate_adv(en):
    translate = {'zero': 'ноль',
                 'one': 'один',
                 'two': 'два',
                 'three': 'три',
                 'four': 'четыре',
                 'five': 'пять',
                 'six': 'шесть',
                 'seven': 'семь',
                 'eight': 'восемь',
                 'nine': 'девять',
                 'ten': 'десять'}
    ru = translate.get(en.lower())
    if en[0].isupper():
        print(f'{en} ---> {ru.title()}')
    else:
        print(f'{en} ---> {ru.lower()}')


num_translate_adv('ten')
num_translate_adv('Nine')
