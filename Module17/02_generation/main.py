long_list = int(input('Введите длину списка: '))
list = list(range(long_list))
list = [x * 0 + 1 if x % 2 == 0 else x % 5 for x in range(long_list)]
print(list)
