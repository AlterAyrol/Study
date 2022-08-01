couple = int(input('Введите количество пар слов: '))
synonyms_dict = {}
for i in range(couple):
    print(i+1, 'пара: ', end = '')
    work_couple = input('').title().split(' — ')
    synonyms_dict[work_couple[0]] = work_couple[1]
    synonyms_dict[work_couple[1]] = work_couple[0]

while True:
    word = input('Введите слово: ').title()
    if word in synonyms_dict.keys():
        print('Синоним:', synonyms_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')
