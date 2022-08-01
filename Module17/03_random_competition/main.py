import random
team1_list = [round(random.random() * 5 + 5, 2) for _ in range(20)]
team2_list = [round(random.random() * 5 + 5, 2) for _ in range(20)]
comparesion_list = [team1_list[x] if team1_list[x] > team2_list [x] else team2_list[x] for x in range(20)]
print('Первая команда:', team1_list)
print('Вторая команда:', team2_list)
print('Победители тура:', comparesion_list)
