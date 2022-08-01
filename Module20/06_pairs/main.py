
import random


original_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', original_list)

new_list = [(original_list[x], original_list[x+1]) for x in range(0, len(original_list), 2)]
print('Новый список:', new_list)

new_list2 = [(original_list[i], original_list[i+1]) for i, val in enumerate(original_list) if not i % 2]
print('Новый список:', new_list2)

