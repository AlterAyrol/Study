import time
from typing import Callable, Any


def Slowpoke(func: Callable, *args, **kwargs) -> Any:
    '''
    Слоупок функция, которая ничего не делает, просто тянет время и этим показывает сложность кода и вычислений)
    :param func: какая-то функция, которая действительно работает)
    :param args:
    :param kwargs:
    :return: func
    '''
    def wrapped_func(*args, **kwargs) -> Any:
        for _ in range(5):
            print("Я ещёёёёё дууууумаюююююю....")
            time.sleep(1)
        print("Я обдуууууумал и начинааааааю рабооооооотаааааать\n")
        func(*args, **kwargs)
    return wrapped_func


@Slowpoke
def test():
    print('<Тут что-то происходит...>')


test()