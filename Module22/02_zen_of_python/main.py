new_reverse_zen = open('reverse_zen.txt', 'w')
new_reverse_zen.close()
# иначе при допиливании напильников в файле reverse_zen появляется несколько десятков
# килограмм философии и его открытие начинает притормаживаться дзеном файла:)


start_zen = open('zen.txt', 'r')
new_reverse_zen = open('reverse_zen.txt', 'a')
for i_line in reversed(start_zen.readlines()):
    new_reverse_zen.write(i_line)
start_zen.close()
new_reverse_zen.close()


new_reverse_zen = open('reverse_zen.txt', 'r')
for i_line in new_reverse_zen:
    print(i_line, end = '')
new_reverse_zen.close()

