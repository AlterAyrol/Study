import random

num_sum = 0

try:
    with open('out_file.txt', 'a') as out_file:
        while num_sum < 777:
            new_num = int(input('Введите число: '))
            a = random.randint(1, 13)
            assert a != 13
            out_file.write(str(new_num)+'\n')
            num_sum += new_num
except AssertionError:
    print('Вас постигла неудача!')
finally:
    print(f"Игра завершена. Вы набрали {num_sum} очков.")


