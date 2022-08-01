import itertools

#Изначальный вариант нежизнеспособен( Зато Появилось ещё 2:)
# st1 = 0
# l1 = itertools.permutations('0123456789', 4)
# for i in l1:
#     st1 += 1
#     print(st1, i)


st2 = 0
l2 = itertools.product('0123456789', repeat = 4)
for i in l2:
    st2 += 1
    print(st2, i)


for i in range(10000):
   print(i, str(i).rjust(4, "0"))  #формирет строку из 4 символов,
                                    # дополняя недостающие до 4х символов элементы нулями.