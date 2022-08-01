violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


songs_quantity = int(input('Сколько песен выбрать? '))
time = 0
for i in range(songs_quantity):
    print('Название', i + 1, 'песни: ', end = '')
    title = input('')
    if title in violator_songs:
        time += violator_songs.get(title)
    else:
        print('Нет такой песни в вашем списке!')
print('Общее время звучания песен: ', round(time, 2), ' минуты.', sep = '')