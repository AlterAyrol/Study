def customer(input):
    work_input = input.split()      #work_input[x]--> 0 - фамилия, 1 - пицца, 2 - кол-во пиццы
    if work_input[0] in customer_dict:
        if work_input[1] in customer_dict[work_input[0]]:
            customer_dict[work_input[0]][work_input[1]] = int(customer_dict[work_input[0]][work_input[1]]) + int(work_input[2])
        else:
            customer_dict[work_input[0]].update({work_input[1]: work_input[2]})
    else:
        customer_dict[work_input[0]] = {work_input[1]: work_input[2]}


order_count = int(input('Введите количество заказов: '))
customer_dict = {}
for i in range(order_count):
    print('Заказ вводится по принципу фамилия, название пиццы, количество штук.')
    print(i + 1, 'заказ: ', end = '')
    order = input('')
    customer(order)

for i in customer_dict:
    print(i, ':', sep = '')
    for i_2 in customer_dict[i]:
        print('\t', i_2, ':', customer_dict[i][i_2])
    print()