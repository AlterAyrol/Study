import functools
from typing import Callable, Any

def debug(func: Callable, *args, **kwargs) -> Any:
    '''
    Фукнция, которая отображает имя выполняемой в ней функции и что она в данный момент делает.
    :param func:
    :param args:
    :param kwargs:
    :return:
    '''
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print("Вызывается функция:", repr(func.__name__))
        print(func.__name__, 'вернула значение:', func(*args, **kwargs))
        func(*args, **kwargs)
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)