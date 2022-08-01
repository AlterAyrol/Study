start_num_list = []
work_list = []

num_amd = int(input('Кол-во чисел: '))
for num in range(num_amd):
    print(num + 1, "-е число: ", end = '', sep = '')
    new_num = int(input())
    start_num_list.append(new_num)
print('Последовательность:', start_num_list)

work_list.append(start_num_list[- 1])
for num in range(num_amd):
    if start_num_list[-num - 1] == start_num_list[-num - 2]:
        work_list.append(start_num_list[num - 2])
    else:
        break
need_input = len(start_num_list) - len(work_list)
print('Нужно приписать чисел:', need_input)


start_num_list.remove(start_num_list[-1])
print(start_num_list)


