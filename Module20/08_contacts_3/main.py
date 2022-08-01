def add_man():
    new_man = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
    if new_man not in contact_dict:
        new_namber = int(input('Введите номер телефона: '))
        contact_dict[new_man] = new_namber
    else:
        print('Такой человек уже есть в контактах.')

def find_man():
    find = input('Введите имя и фамилию нового контакта (через пробел): ').title()
    for i_name in contact_dict:
        if find in i_name:
            print(i_name[0], i_name[1], contact_dict[i_name])

contact_dict ={('Иван', 'Сидоров'): 888}

while True:
    action = int(input('Введите номер действия: \n\t1. Добавить контакт \n\t2. Найти человека \n'))
    if action == 1:
        add_man()
    elif action == 2:
        find_man()
    else:
        print("Неверно указано действие!")
    print('Текущий словарь контактов:', contact_dict)