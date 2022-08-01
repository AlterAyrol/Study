def guests_exist(check_guest, all_guests):
    for i_guests in range(len(all_guests)):
        if all_guests[i_guests] == check_guest:
            return True
    return False

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    guests_question = input('Гость пришёл или ушёл? ')
    if guests_question == 'Пора спать':
        break
    guest_name = input('Имя гостя: ')
    if guests_question == 'пришёл':
        if len(guests) > 5:
            print('Прости,', guest_name, 'но мест нет.')

        else:
            print('Привет,', guest_name + '!')
            guests.append(guest_name)

    elif guests_question == 'ушёл':
        if guests_exist(guest_name, guests):
            print('Пока,', guest_name + '!')
            guests.remove(guest_name)

        else:
            print("Такого гостя у вас на вечеринке нет!")

    else:
        print("Неправильная команда!")

print('Вечеринка закончилась, все легли спать.')