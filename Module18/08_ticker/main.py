def work_row(r1, r2):
    work_shift = 1
    if r1 == r2:
        return work_shift
    elif r1 != r2:
        for _ in range(len(r2)):
            work_shift += 1
            r2 = r2[-1] + r2[:-1]
            if r1 == r2:
                break
    return work_shift

row1 = input('Первая строка: ')
row2 = input('Вторая строка: ')

shift = work_row(row1, row2)

if shift > len(row2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print('Первая строка получается из второй со сдвигом', shift - 1)


