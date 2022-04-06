list_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
string = ''
list_fix = []
x = 0
for item in list_text:
    for i in item:
        if not i.isdigit():
            string = f'{string}{i}'
        elif i.isdigit() and x == 1:
            string = f'"{item}"'
        else:
            string = f'"{string}0{i}"'
            x = 1
    x = 0
    list_fix.append(string)
    string = ''
print(' '.join(list_fix))
