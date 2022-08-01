import functools
from typing import Callable, Any


count = [1]


def counter(func: Callable, *args, **kwargs) -> Any:
    '''
    Выполняет какую-то функцию и выводит какой раз её выполняет.
    :param func:
    :param args:
    :param kwargs:
    :return: func
    '''
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print("Функция вызывается", count[0], "раз.")
        func(*args, **kwargs)
        count[0] += 1
    return wrapped_func


@counter
def test() -> None:
    '''
    Функция для теста и отображения случайного текста.
    :return: None
    '''
    print('<Тут что-то происходит...>')


test()
test()
test()
test()



