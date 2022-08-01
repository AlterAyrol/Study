import os

text = input('Введите строку: ')
where_save = str(input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n'))
file_name = input('Введите имя файла: ')

testpath = where_save.replace(" ", "/")
path = os.path.abspath(os.path.join(os.path.sep, testpath, file_name + '.txt'))

with open(path, 'w') as new_file:
    new_file.write(text)
