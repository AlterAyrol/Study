from abc import ABC, abstractmethod


class MyMath(ABC):
    """
    Мини аналог модуля math
    """
    def circle_len(radius: float) -> float:
        len = 3.1415926535 * 2 * radius
        return  len


    def circle_sq(radius: float) -> float:
        sq = 3.1415926535 * radius ** 2
        return sq


    def cube_volume(volume: float) -> float:
        vol = volume ** 3
        return vol


    def sphere_sq(radius: float) -> float:
        sq = 4 * 3.1415926535 * radius ** 2
        return sq


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)