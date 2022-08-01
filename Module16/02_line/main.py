#Хоте сделать, что бы сразу учеников из второго класса ставило на нужное место, но не получилось(

class1 = list(range(160, 177, 2))
class2 = list(range(162, 180, 3))
class1.extend(class2)
for _ in range(len(class1) - 1):
    for height in range(len(class1) - 1):
        if class1[height + 1] < class1[height]:
            class1[height + 1], class1[height] = class1[height], class1[height + 1]

print('Отсортированный список учеников:', class1)

# for height1 in class1:
#     for height2 in class2:
#         if height2 > height1:
#             class1.insert(class1.index(height1) + 1, height2)
#             class2.remove(height2)
#         elif height2 < height1:
#             class1.insert(class1.index(height1), height2)
#             class2.remove(height2)





