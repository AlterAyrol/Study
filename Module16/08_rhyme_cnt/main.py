# Не могу понять, почему на 15 строке цикл while уходит в бесконечный цикл. Уходит только при индексе равнмым
#     нулю. Специально добавил условия про не равен нулю, но всё равно зависает. Помогите разобраться в корне проблемы.

people_amd = int(input('Кол-во человек: '))
people_list = list(range(1, people_amd + 1))

reader_num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ', reader_num, '-й человек.', sep = '')

while len(people_list) > 1:
    print('\nТекущий круг людей:', people_list)
    start = int(input('Начало счёта с номера? '))
    index = people_list.index(start)
    index = index + reader_num - len((people_list))

    while (index > len(people_list)) and (index != 0):
        index = index + reader_num - len((people_list))


    print('Выбывает человек под номером', people_list[index - 1])
    people_list.remove(people_list[index - 1])

print('Остался человек под номером ', people_list)

