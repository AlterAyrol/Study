def find_country(town, countrys):
    for i in range(len(countrys)):
        if town in countrys[i]:
            return countrys[i][0]
    return False

country_quantity = int(input('Количество стран: '))
country_list = []
for i in range(country_quantity):
    print(i + 1, 'страна: ', end = '')
    country = input('').split()
    country_list.append(country)

for i in range(3):
    print(i + 1, 'город: ', end = '')
    find_town = input('')
    country = find_country(find_town, country_list)
    if not country:
        print('По городу', find_town, 'данных нет.')
    else:
        print('Город ', find_town, ' расположен в стране ', country, '.', sep = '')
