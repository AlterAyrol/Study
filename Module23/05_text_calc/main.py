with open('calc.txt', 'w') as calc:
    text = '''100 + 34
10 +* 3
20 -* 2
23 / 4'''
    calc.write(text)


def calc_line(line):
    work_line = line.split()
    try:
        if work_line[0].isdigit() and work_line[2].isdigit():
            try:
                if work_line[1] == '+':
                    calc_sum[0] += int(work_line[0]) + int(work_line[2])
                elif work_line[1] == '-':
                    calc_sum[0] += int(work_line[0]) - int(work_line[2])
                elif work_line[1] == '*':
                    calc_sum[0] += int(work_line[0]) * int(work_line[2])
                elif work_line[1] == '/':
                    calc_sum[0] += int(work_line[0]) / int(work_line[2])
                else:
                    raise NameError
            except NameError:
                print(f'Обнаружена ошибка в строке: {line}.')
                choice = input('Хотите исправить? ')
                if choice.lower() == "да":
                    true_line = input('Введите исправленную строку:')
                    calc_line(true_line)
        else:
            raise NameError
    except NameError:
        print(f'Обнаружена ошибка в строке: {line}')
        choice = input('Хотите исправить? ')
        if choice.lower() == "да":
            true_line = input('Введите исправленную строку:')
            calc_line(true_line)
        else:
            return None

calc_sum = [0]

try:
    with open('calc.txt', 'r') as calc:
        for i_line in calc:
            work_sum = calc_line(i_line)


finally:
    print('Сумма результатов:', str(calc_sum[0]))