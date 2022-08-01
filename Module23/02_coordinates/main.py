import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            try:
                with open('result.txt', 'a') as file_2:
                    my_list = sorted([res1, res2, number])
                    file_2.write(str(my_list)+'\n')
            except Exception:
                print("Что-то пошло не так со второй функцией")
except ZeroDivisionError:
    print("При вызове рандомного числа произошло деление на ноль")
except FileNotFoundError:
    print("Файла coordinates.txt не найдено")
except Exception:
    print("Что-то пошло не так с первой функцией")

try:
    with open('result.txt', 'r') as file_2:
        for i in file_2:
            print(i)
except Exception:
    print("Что-то пошло не так")



