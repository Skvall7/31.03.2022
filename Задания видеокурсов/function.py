def user(name, age, city):
    return f'{name}, {age} год, проживает в городе {city}'


users = ['Антон', '36', 'Чебоксары']
print(user(users[0], users[1], users[2]))


def digit(first, second, third):
    return max(int(first), int(second), int(third))


numbers = [10, '123', 5]
print(digit(numbers[0], numbers[1], numbers[2]))

name = input('Введите имя: ')
player = {'name': name, 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': 'Страшный', 'health': 110, 'damage': 40, 'armor': 1.3}
print(player, enemy)


def attack(player_1, player_2):
    def clear_damage(player_1_d, player_2_a):
        player_1_d['damage'] /= player_2_a['armor']
        return int(player_1_d['damage'])
    save = player_1['damage']
    player_2['health'] -= clear_damage(player_1, player_2)
    player_1['damage'] = save
    return player_1, player_2


print(attack(enemy, player))
print(attack(player, enemy))
