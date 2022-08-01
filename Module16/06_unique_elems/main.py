list1 = []
list2 = []

for i_num in range(3):
    print('Введите ', i_num + 1, '-е число для первого списка: ', end = '', sep = '')
    num = int(input())
    list1.append(num)

for i_num in range(7):
    print('Введите ', i_num + 1, '-е число для первого списка: ', end = '', sep = '')
    num = int(input())
    list2.append(num)


print('Первый список:', list1)
print('Второй список:', list2)

list1.extend(list2)


for i_num in range(len(list1)):
    while list1.count(i_num) > 1:
        list1.remove(i_num)

print(list1)
