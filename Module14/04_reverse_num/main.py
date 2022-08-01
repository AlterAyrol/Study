def reverse_num(num):
    pre_point = ""
    after_point = ''
    point_flag = False
    for i in str(num):
        if i == '.':
            point_flag = True
        if point_flag == False:
            pre_point = i + pre_point
        elif point_flag == True and i != ".":
            after_point = i + after_point
    return (pre_point + '.' + after_point)



num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
print('\nПервое число наоборот:', reverse_num(num1))
print('Второе число наоборот:', reverse_num(num2))
sum_reverse_num = float(reverse_num(num1)) + float(reverse_num(num2))
print('Сумма:', sum_reverse_num)
