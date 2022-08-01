import random

def game(stick, throw):
    result_list = [1 for _ in range(stick)]
    for _ in range(throw):
        left_i = random.randint(0, stick)
        right_i = random.randint(0, stick)
        if left_i > right_i:
            left_i, right_i = right_i, left_i
        result_list = [result_list[x] * 0 if round(random.random(), 0) == 1 and left_i <= x <= right_i
                       else result_list[x] * 1 for x in range(stick)]
    return result_list

def change(sym):
    if sym == 1:
        sym = 'I'
    elif sym == 0:
        sym = '.'
    return sym


stick_amount = int(input('Количество палок: '))
throw_amount = int(input('Количество бросков: '))

result = game(stick_amount, throw_amount)

if sum(result) == 0:
    print('STRIIIIKE :)')
else:
    for x in result:
         print(change(x), end = '')


