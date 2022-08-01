# Пробовал через превращение поступающей информации в list и оттуда путём [number:] и до второго повторения
# [:number] , но не получилось. Вышел достаточно громоздкий, на мой взгляд, код. Работает. Но уверен, что
# его можно упростить(

def slicer(test_tuple, number):
    answer = []
    start_stop_flag = False
    count = 0
    for i in test_tuple:
        if start_stop_flag == True:
            answer.append(i)
        if i == number and start_stop_flag == True and count == 1:
            start_stop_flag = False
        if i == number and start_stop_flag == False and count == 0:
            answer.append(i)
            start_stop_flag = True
            count += 1
    return tuple(answer)


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))



# def slicer(any_tuple, element):
#     if element in any_tuple:
#         if any_tuple.count(element) > 1:
#             first_index = any_tuple.index(element)
#             second_index = any_tuple.index(element, first_index + 1) + 1
#             return any_tuple[first_index:second_index]
#         else:
#             return any_tuple[any_tuple.index(element):]
#     else:
#         return ()
#
# # print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))