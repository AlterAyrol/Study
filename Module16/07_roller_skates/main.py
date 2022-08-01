def sort_list(list):
    for _ in range(len(list) - 1):
        for i_list in range(len(list) - 1):
            if list[i_list + 1] > list[i_list]:
                list[i_list + 1], list[i_list] = list[i_list], list[i_list + 1]
    return list

skates_list = []
legs_list = []
count = 0
skates_start = 0

skates_sum = int(input('Кол-во коньков: '))
for i_skates in range(skates_sum):
    print('Размер ', i_skates + 1, '-й пары: ', end = '', sep = '')
    skates = int(input())
    skates_list.append(skates)

legs_sum = int(input('Кол-во людей: '))
for i_legs in range(legs_sum):
    print('Размер ноги ', i_legs + 1, '-го человека: ', end = '', sep = '')
    legs = int(input())
    legs_list.append(legs)

sort_list(skates_list)
sort_list(legs_list)

for i_legs in legs_list:
    if skates_start > len(skates_list):
        break
    if skates_list[skates_start] >= i_legs:
        count += 1
        skates_start += 1

print(count)
