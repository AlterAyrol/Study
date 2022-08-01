from typing import Callable, Any
import functools


def do_func(func: Callable) -> Callable:
    """
    Черновой вариант декоратора, который каким-то образом и так прекрасно работает и выполняет
    поставленную задачу. "Работает - не трогай(с)."
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        func()
    return wrapped_func


@do_func
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)
