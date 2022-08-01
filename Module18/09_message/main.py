def reverse_text(input_text):
    return input_text[::-1]

text = input('Сообщение: ')

work_word = ''
work_text = ''
work_sym = ',.:; !?'

for x in text:
    if x not in work_sym:
        work_word += x
    elif x in work_sym:
        work_text += reverse_text(work_word) + x
        work_word = ''

print('Новое сообщение:', work_text)

