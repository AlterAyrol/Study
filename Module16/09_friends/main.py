friends_amd = int(input("Кол-во друзей: "))
friends_amd_list = []
for _ in range(friends_amd):
    friends_amd_list.append(0)

debt_receipts = int(input('Долговых расписок: '))

for debt in range(debt_receipts):
    print('\n', debt + 1, '-я расписка.', sep = '')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    if (to_whom > len(friends_amd_list)) or (from_whom > len(friends_amd_list)):
        print("Нет такого друга.")
    else:
        friends_amd_list[to_whom - 1] = friends_amd_list[to_whom - 1] + how_many
        friends_amd_list[from_whom - 1] = friends_amd_list[from_whom - 1] - how_many

print('Баланс друзей:')
for i_frend in range(len(friends_amd_list)):
    print(i_frend + 1, ': ', friends_amd_list[i_frend], sep = '', end = '\n')

