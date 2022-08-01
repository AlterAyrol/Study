def smallest_divisor(num):
    divisor_start = 2
    while num % divisor_start != 0:
        divisor_start += 1
    return divisor_start

find_num = int(input("Введите число: "))
smallest_divisor = smallest_divisor(find_num)
print('Наименьший делитель, отличный от единицы:', smallest_divisor)
