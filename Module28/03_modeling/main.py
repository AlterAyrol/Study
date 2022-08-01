import math

class Triangle:
    '''
    Класс создающий и описывающий фигуру - Треугольник
    '''
    def __init__(self, basis: (float, int), height: (float, int)) -> None:
        self.__basis = basis
        self.__height = height

    def __str__(self) -> str:
        return f"Треугольник с основанием: {self.__basis} и высотой: {self.__height}." \
               f" Периметр: {Triangle.triangle_perimeter(self)}." \
               f" Площадь: {Triangle.triangle_square(self)}."

    @property
    def basis(self) -> (float, int):
        return self.__basis

    @property
    def height(self) -> (float, int):
        return self.__height

    @basis.setter
    def basis(self, new_basis: (float, int)) -> None:
        self.__basis = new_basis

    @height.setter
    def height(self, new_height: (float, int)) -> None:
        self.__height = new_height

    def triangle_square(self) -> (float, int):
        square = 0.5 * self.__basis * self.__height
        return square

    def triangle_perimeter(self) -> (float, int):
        hypotenuse = math.sqrt((0.5 * self.__basis) ** 2 + self.__height ** 2)
        perimeter = self.__basis + hypotenuse * 2
        return perimeter


class Square:
    """
    Класс создающий и описывающий фигуру - Квадрат
    """
    def __init__(self, side: (float, int)) -> None:
        self.__side = side

    def __str__(self) -> str:
        return f'Квадрат с длинной стороны: {self.__side}. ' \
               f'Периметр: {Square.square_perimeter(self)}. Площадь: {Square.square_sq(self)}'

    @property
    def side(self) -> (float, int):
        return self.__side

    @side.setter
    def side(self, new_side: (float, int)) -> None:
        self.__side = new_side

    def square_sq(self) -> (float, int):
        sq = self.__side ** 2
        return sq

    def square_perimeter(self) -> (float, int):
        perimeter = self.__side * 4
        return perimeter


class Cube:
    """
    Класс создающий и описывающий фигуру - Куб
    """
    def __init__(self, side: (float, int)) -> None:
        self.__side = side
        self.__cube = [Square(side) for _ in range(6)]

    def __str__(self) -> str:
        return f"Куб с длинной стороны: {self.__side}. Площадь: {Cube.cube_sq(self)}."

    @property
    def side(self) -> (float, int):
        return self.__side

    @side.setter
    def side(self, new_side: (float, int)) -> None:
        self.__side = new_side
        self.__cube = [Square(new_side) for _ in range(6)]

    def cube_sq(self) -> (float, int):
        sq = self.__side ** 2 * 6
        return sq


class Pyramid:
    """
    Класс создающий и описывающий фигуру - Пирамида
    """
    def __init__(self, basis: (float, int), height: (float, int)) -> None:
        self.__basis = basis
        self.__height = height
        self.__pyramid = [Triangle(basis, height) for _ in range(4)]

    def __str__(self) -> str:
        return f"Пирамида с основанием: {self.__basis} и апофемой: {self.__height}." \
               f" Площадь: {Pyramid.pyramid_sq(self)}."

    @property
    def basis(self) -> (float, int):
        return self.__basis

    @property
    def height(self) -> (float, int):
        return self.__height

    @basis.setter
    def basis(self, new_basis: (float, int)) -> None:
        self.__basis = new_basis
        self.__pyramid = [Pyramid(new_basis, self.height) for _ in range(4)]

    @height.setter
    def height(self, new_height: (float, int)) -> None:
        self.__height= new_height
        self.__pyramid = [Pyramid(self.basis, new_height) for _ in range(4)]

    def pyramid_sq(self) -> (float, int):
        triangle_square = 0.5 * self.__basis * self.__height
        basis_square = self.__basis ** 2
        pyramid_sq = triangle_square * 4 + basis_square
        return pyramid_sq


cub = Cube(5)
print(cub)
pyr = Pyramid(4, 7)
print(pyr)