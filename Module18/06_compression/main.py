text = input('Введите строку: ')

work_text = [text[x] if text[x] == text[x+1] else text[x]+'!' for x in range(len(text) - 1) ]
work_text.append(text[-1])

work_text = ''.join(work_text)
work_text = work_text.split('!')

print('Закодированная строка:', end =' ')
for i in range(len(work_text)):
    print(work_text[i][0], len(work_text[i]), end = '', sep = '')


