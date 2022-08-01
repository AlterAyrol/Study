def special_years(num):
    n1 = num  // 1000
    n2 = num //100 % 10
    n3 = num //10 % 10
    n4 = num % 10
    special = 0
    if (n1 == n2 == n3) or (n1 == n2 == n4) or (n2 == n3 == n4) or (n1 == n3 == n4):
        special = num
        print(special)

num_start = int(input('Введите первый год: '))
num_fin = int(input('Введите второй год: '))
for i in range(num_start, num_fin + 1):
    special_years(i)


