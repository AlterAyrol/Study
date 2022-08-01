

def Fibonachi(stop_insert, pre_num = - 1, num = 1,stop_count = 0):
    if stop_insert == stop_count:
        return pre_num + num
    result = pre_num + num
    return Fibonachi(stop_insert, num, result, stop_count + 1)


fib = Fibonachi(int(input('Введите позицию числа в ряде Фибоначчи: ')))
print(fib)