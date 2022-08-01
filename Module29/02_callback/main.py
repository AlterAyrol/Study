from typing import Callable, Any
import functools


app = {}


def callback(route: str) -> Callable:
    """ Декоратор обратного вызова """
    def wrapper(func: Callable) -> Any:
        app[route] = func
    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')