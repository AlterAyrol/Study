import random, os
with open('karma.log.txt', 'w') as karma_log:
    karma_log.write('Начало файла')


def one_day():
    karma_points = random.randint(1, 8)
    if karma_points == 8:
        error_num = random.randint(0, 4)
        return (karma_points + error_num)
    else:
        return karma_points

def life():
    work_karma = 0
    day = 1
    while work_karma < 500:
        day += 1
        work_num = one_day()
        print(f"\nУ вас уже {work_karma} из 500.")
        if 1<=work_num<=7:
            work_karma += one_day()
            print(f"За сегодня вы получили {work_num} кармы.")
        else:
            error_list = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
            error_text = "Вас постигла карма - " + error_list[work_num-8] + f' на {day} день!' + "\n"
            with open('karma.log.txt', 'a') as karma_log:
                karma_log.write(error_text)
    return print(f"Вы постигли дзен на {day} день. Поздравляем!")

life()

