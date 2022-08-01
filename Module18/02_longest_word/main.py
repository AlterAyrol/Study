text = input('Введите строку: ').split()

longest_word = [len(text[x]) for x in range(len(text))]

print('Самое длинное слово:', text[longest_word.index(max(longest_word))])

print('Длина этого слова:', max(longest_word))
