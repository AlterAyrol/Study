from typing import Callable, Any
import datetime
import functools


def logging(func: Callable, *args, **kwargs) -> Any:
    '''
    Функция, которая пробует выполнить любую другую. При успехе возвращает имя функции, её описание и результат её
    работы. При неудаче, записывает в лог имя функции и дату выполнения.
    :param func:
    :param args:
    :param kwargs:
    :return:
    '''
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(func.__name__)
            print(func.__doc__)
            func(*args, **kwargs)
        except:
            with open('function_errors.log', 'a') as error_file:
                time = str(datetime)
                name = func.__name__
                error_file.write(time + name + '\n')
    return wrapped_func


@logging
def test():
    '''
    Функция для теста и отображения случайного текста.
    :return: None
    '''
    print('<Тут что-то происходит...>')


test()





