work_list = []
def sum(*args):
    for i in args:
        if isinstance(i, list):
            sum_list(i)
        elif isinstance(i, int) or isinstance(i, float):
            work_list.append(i)
        elif isinstance(i, tuple):
            sum_tuple(i)
    sum_num = 0
    for i, val in enumerate(work_list):
        sum_num += val
    print('Ответ в консоли:', sum_num)

def sum_list(something_list):
    if isinstance(something_list, int) or isinstance(something_list, float):
        work_list.append(something_list)
    if isinstance(something_list, list):
        for part in something_list:
            sum_list(part)

def sum_tuple(something_tuple):
    if isinstance(something_tuple, int) or isinstance(something_tuple, float):
        work_list.append(something_tuple)
    if isinstance(something_tuple, tuple):
        for part in something_tuple:
            sum_tuple(part)


# мне показалось, так будет сложнее, реализовал для теста такую версию
sum(1, ((2, 3), 4, (5), 6), 7, 8, [9, [10, [11]], 12])


