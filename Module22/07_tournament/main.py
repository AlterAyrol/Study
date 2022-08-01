def count_elem(elem):
    return elem[2]

second_tour = open('second_tour.txt', 'w')
second_tour.close()
#для удаления всех данных в файле при тестах

with open('first_tour.txt', 'w') as first_tour:
    base = '''80
Ivanov Serg 80
Sergeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78
'''
    first_tour.write(base)

second_tour_list = []

with open('first_tour.txt', 'r') as first_tour:
    for i_first_tour_len, val_first_tour in enumerate(first_tour):
        if i_first_tour_len == 0:
            border = int(val_first_tour)
        if i_first_tour_len > 0:
            work_list = val_first_tour.split()
            if int(work_list[2]) > border:
                name = work_list[1]
                name = name[0] + '.'
                work_list[1] = name
                second_tour_list.append([work_list[1], work_list[0], work_list[2]])

with open('second_tour.txt', 'a') as second_tour:
    second_tour_list.sort(key = count_elem, reverse=True)
    second_tour.write(str(len(second_tour_list)))
    for i_second_tour_list, val_second_tour_list in enumerate(second_tour_list):
        val = str(f'{val_second_tour_list[0]} {val_second_tour_list[1]} {val_second_tour_list[2]}')
        work_list = str(f'\n{i_second_tour_list + 1}) {val}')
        second_tour.write(str(work_list))

with open('second_tour.txt', 'r') as second_tour:
    for i in second_tour:
        print(i, end = '')