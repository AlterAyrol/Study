string = 'a(bc'
nums_tuple = (10, 20, 30, 40)

new_tuple_list = []
for i, val in enumerate(string):
    new_tuple_list.append((val, nums_tuple[i]))
new_tuple_list = tuple(new_tuple_list)
print('Заменитель zip')
print(tuple(new_tuple_list))
for i, val in enumerate(new_tuple_list):
    print(val)

normal_python_zip = zip(string, nums_tuple)
print(normal_python_zip)
print('\nНормальная zip')
for i, val in enumerate(normal_python_zip):
    print(val)