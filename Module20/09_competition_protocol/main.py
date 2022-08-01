def check(name, score):
    if sum(map(int, str(score))) > sum(map(int, str(players_dict[name]))):
        return True

def champions():
    for player, score in players_dict.items():
        if sum(map(int, str(score))) > sum(map(int, str(champion_dict[3][1]))):
            champion_dict[3] = (player, score)
        if sum(map(int, str(score))) > sum(map(int, str(champion_dict[2][1]))):
            champion_dict[3], champion_dict[2] = champion_dict[2], champion_dict[3]
        if sum(map(int, str(score))) > sum(map(int, str(champion_dict[1][1]))):
            champion_dict[2], champion_dict[1] = champion_dict[1], champion_dict[2]


players = int(input('Сколько записей вносится в протокол? '))
players_dict = {}
print('Записи (результат и имя):')
for i in range(1, players + 1):
    new_player = input(f'{i}-я запись: ').split()
    if new_player[1] in players_dict:
        if check(new_player[1], new_player[0]):
            players_dict[new_player[1]] = int(new_player[0])
    else:
        players_dict[new_player[1]] = int(new_player[0])

champion_dict = {1: ('', 0), 2: ('', 0), 3: ('', 0)}
champions()

print('Итоги соревнований:')
for place, player in champion_dict.items():
    print(f'{place}-е место: {player[0]} со счётом {player[1]}')

