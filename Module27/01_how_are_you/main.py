from typing import Callable, Any


def how_are_you(func: Callable, *args, **kwargs) -> Any:
    """
    Функция паразит)
    :param func: функция, которая действительно работает
    :param args:
    :param kwargs:
    :return: func
    """
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrapped_func


@how_are_you
def test() -> None:
    '''
    Функция для теста и отображения случайного текста.
    :return: None
    '''
    print('<Тут что-то происходит...>')


test()