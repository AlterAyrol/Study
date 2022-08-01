
max_num = int(input('Введите максимальное число: '))
work_set = {'0'}
first_answer_flag = True
true_num = int(input('Артём, введи загадываемое число: '))
if true_num not in list(range(1, max_num)):
    print('Артём, ты загадал число, которого нет в списке максимальных чисел!')
else:
    max_num = list(range(1, max_num + 1))
    while True:
        work_numbers = input('Нужное число есть среди вот этих чисел (вводите числа через пробел): ')
        if work_numbers.lower() == 'помогите':
            print('Артём мог загадать следующие числа:', work_set)
        answer = input('Ответ Артёма: ').lower()
        # if (answer.lower == "да" and true_num not in work_numbers) or (answer.lower == "нет" and true_num in work_numbers):
        #     print(f'Артём соврал! Он загадал {true_num}!')
        #     break                                        #не могу понять, что именно тут не срабатывает
        if answer.lower() == "да" and first_answer_flag == True:
            work_set.update(work_numbers)
            work_set -= {'0', ' ', ''}
            first_answer_flag = False
        elif answer.lower() == 'нет':
            work_set -= set(work_numbers)
        print(work_set)