test_family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Смирнов", "Артём"): 12
}

find_surname = input('Введите фамилию: ')
for i_surname in test_family:
    if find_surname.title() in i_surname or find_surname[:-1].title() in i_surname\
            or ((find_surname + 'а').title() in i_surname):
        print(i_surname, test_family[i_surname])
