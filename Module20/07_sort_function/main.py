def tpl_sort(input_tuple):
    for i_num in input_tuple:
        if not isinstance(i_num, int):
            return input_tuple
        return tuple(sorted(input_tuple))


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))


# В предложенном для работы примере не хватает скобок. Долго не мог понять, почему не работает функция.
# Выдавало ошибку: TypeError: tpl_sort() takes 1 positional argument but 7 were given
# print(tpl_sort(6, 3, -1, 8, 4, 10, -5))