with open('people.txt', 'w') as people:
    text = '''Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина
'''
    people.write(text)

letter_count = 0
line_count = 0
try:
    with open('people.txt', 'r') as people:
        for i_line in people:
            line_count += 1
            for i_letter in i_line:
                if i_letter.isalpha():
                    letter_count += 1
            try:
                assert (len(i_line) - 1 != 1) and (len(i_line) - 1 != 2)
            except AssertionError:
                print(f'Ошибка: длинна строки {line_count} менее трёх символов!')

except FileNotFoundError:
    print("Файл не найден")

finally:
    print('Общее количество символов:', letter_count)





