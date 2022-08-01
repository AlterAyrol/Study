
family = {}
pair_count = int(input('Введите количество человек: '))
for i in range(1, pair_count):
    child_name, parent_name = input(f'{i} пара: ').split()
    if parent_name not in family:
        family[parent_name] = 0
    if child_name not in family:
        family[child_name] = family[parent_name] + 1
for i in sorted(family.keys()):
    print(i, family[i])