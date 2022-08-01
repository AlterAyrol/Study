def code(sym, step):
    alpahbet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if sym in alpahbet:
        i_sym = alpahbet.index(sym)
        i_sym += step
        if i_sym >= len(alpahbet):
            i_sym = i_sym - len(alpahbet)
        sym = alpahbet[i_sym]
        return sym
    else:
        return sym

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

secret_text = [code(x, shift) for x in text]

print('Зашифрованное сообщение: ', end = '')
for i in secret_text:
    print(i, end = '')


