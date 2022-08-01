from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def input(*args: Any, **kwargs: Any) -> str:
        lst = (args, kwargs)
        print('Переданные арги и кварги в декоратор:', lst)
        def do_func(func) -> Any:
            def wrapped_func(*args, **kwargs) -> Any:
                func(*args, **kwargs)
            return wrapped_func
        return do_func
    return input



@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int):
    print("Привет", text, num)


decorated_function("Юзер", 101)
