import os
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()

path = os.path.abspath(os.path.join('..',  '02_zen_of_python', 'zen.txt'))
with open(path, 'r') as zen:
    len_count = 0
    words_count = 0
    letter_count = 0
    most_rarely_letter = {}
    for i_line in zen:
        len_count += 1
        line = i_line.split()
        for i_words in line:
            words_count += 1
            word = list(i_words)
            for i_letter in word:
                letter_count += 1
                if i_letter in most_rarely_letter:
                    most_rarely_letter[i_letter] += 1
                elif i_letter in alphabet_lower or i_letter in alphabet_upper:
                    most_rarely_letter[i_letter] = 1

print('Количество букв в файле:', letter_count)
print('Количество слов в файле:', words_count)
print('Количество строк в файле:', len_count)
print('Наиболее редкие буквы: ', end = '')
for i, val in most_rarely_letter.items():
    if val == 1:
        print(i, ', ', end = '', sep = '')