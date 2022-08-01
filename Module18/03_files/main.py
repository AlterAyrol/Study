def start(sym):
    if sym in '@№$%^&\*()':
        return True
    return False

file = input('Название файла: ')
if start(file[0]):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file.endswith('.txt') and not file.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')