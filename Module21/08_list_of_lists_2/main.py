work_list = []
def good_list(something_list):
    if isinstance(something_list, int) or isinstance(something_list, float):
        work_list.append(something_list)
    if isinstance(something_list, list):
        for part in something_list:
            good_list(part)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
good_list(nice_list)

print('Ответ:', work_list)

