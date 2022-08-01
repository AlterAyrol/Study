def sequence(seq_sym, count, H_flag):
    if seq_sym == 'h':
        count[0] += 1
    if count[0] >= 1 and count[0] < H_flag:
        return True
    elif count[0] == 0 or count[0] == H_flag:
        return False


text = input('Введите строку: ')
count_start = [0]
H = (list(text)).count('h')

work_text = [x for x in text if sequence(x, count_start, H)    ]

print('Развёрнутая последовательность между первым и последним h:', end = ' ')
for i in range(len(work_text) - 1):
    print(work_text[-i - 1], end = '')

# Пробовал упростить, но не получилось
# print()
# work_text2 = [work_text[-x - 1] for x in range(len(work_text) - 1)]
# print(work_text2)
# print(text[H+1: 0: -1])
