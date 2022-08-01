

def num_row(end_num, start_num = 1):
    if end_num == start_num:
        return end_num
    print(start_num)
    return num_row(end_num, start_num + 1)


new_num = int(input('Введите num: '))
print(num_row(new_num))