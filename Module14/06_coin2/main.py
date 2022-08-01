import math

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
hypotenuse = math.sqrt(x ** 2 + y ** 2)
if hypotenuse <= r:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')

