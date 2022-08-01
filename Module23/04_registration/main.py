def bad_log_save(bad_line, error):
    with open('registrations_bad.log.txt', 'a') as registrations_bad_log:
        text = ''
        for i in bad_line:
            text += i + ' '
        text += error + '\n'
        registrations_bad_log.write(text)

def registrations_good_log(good_line):
    with open('registrations_good.log.txt', 'a') as registrations_good_log:
        text = ''
        for i in good_line:
            text += i + ' '
        text += '\n'
        registrations_good_log.write(text)

def check_line(line):
    try:
        if len(line) == 3:
            try:
                if line[0].isalpha():
                    try:
                        if '@' in line[1] and '.' in line[1]:
                            try:
                                if line[2].isdigit() and 10 <= int(line[2]) <= 99:
                                    registrations_good_log(line)
                                else:
                                    raise ValueError
                            except ValueError:
                                bad_log_save(line, 'Поле «Возраст» НЕ является числом от 10 до 99')
                        else:
                            raise SyntaxError
                    except SyntaxError:
                        bad_log_save(line, 'Поле «Имейл» НЕ содержит @ и . (точку)')
                else:
                    raise NameError
            except NameError:
                bad_log_save(line, 'Поле «Имя» содержит НЕ только буквы')
        else:
            raise IndexError
    except IndexError:
        bad_log_save(line, 'НЕ присутствуют все три поля')



try:
    with open('registrations.txt', 'r', encoding='utf-8') as registrations:
        for i_line in registrations:
            work_line = i_line.split()
            check_line(work_line)


finally:
    print('Сортировка закончена')


