def num_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

def num_lot(num):
    sum = 0
    for i in str(num):
        sum += 1
    return sum

find_number = int(input("Введите число: "))
num_sum = num_sum(find_number)
num_lot = num_lot(find_number)
print('Сумма чисел:', num_sum)
print('Количество цифр в числе:', num_lot)
print('Разность суммы и количества цифр:', num_sum - num_lot)
