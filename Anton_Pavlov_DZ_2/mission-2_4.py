list_member = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
               'директор аэлита']
for i in list_member:
    post = i.split(' ')
    name = post[-1]
    post.remove(name)
    print(f'Привет, {name.title()}!')
