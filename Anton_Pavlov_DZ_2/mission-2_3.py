list_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
string = ''
x, y = 0, 0
length = len(list_text)
for item in list_text:
    if length == y:
        break
    for i in item:
        if not i.isdigit():
            string = f'{string}{i}'
        elif i.isdigit() and x == 1:
            string = f'"{item}"'
        else:
            string = f'"{string}0{i}"'
            x = 1
    list_text.append(string)
    string = ''
    x = 0
    y += 1
while length != len(list_text):
    list_text.pop(0)
print(' '.join(list_text))
