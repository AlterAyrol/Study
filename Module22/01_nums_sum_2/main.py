file_numbers = open('numbers.txt', 'r')
summa = 0
for i_line in file_numbers:
    work = i_line.split()
    if len(work) == 1:
        summa += int(work[0])
file_numbers.close()


file_answer = open('answer.txt', 'w')
file_answer.write(str(summa))
file_answer.close()


file_answer = open('answer.txt', 'r')
print('Содержимое файла answer.txt')
for i_line in file_answer:
    print(i_line)
file_answer.close()
