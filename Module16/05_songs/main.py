def song_exist(check_song, all_songs):
    for i_song in range(len(all_songs)):
        if check_song == all_songs[i_song][0]:
            return True
    return False


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_sum = int(input('Сколько песен выбрать? '))
new_list_time = 0
for i_song in range(songs_sum):
    print('Название ', i_song + 1, '-й', ' песни: ', end = '')
    song = input()

    if song_exist(song, violator_songs):
        for i_song in range(len(violator_songs)):
            if violator_songs[i_song][0] == song:
                new_list_time += violator_songs[i_song][1]

    else:
        print("Такой песни нет в списке!")

print("\nОбщее время звучания песен:", round(new_list_time, 2), 'минуты')