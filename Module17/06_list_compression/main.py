import random

nums = int(input('Количество чисел в списке: '))
nums_list = [int(random.random() * 3) for _ in range(nums)]
print('Список до сжатия:', nums_list)
nums_list_sort = [x for x in nums_list if x != 0]
print('Список после сжатия:', nums_list_sort)