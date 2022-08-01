from typing import Callable, Any
import functools


user_permissions = ['admin']


def check_permission(check: Any) -> Callable:
    '''
    Функция проверки наличия разрешения для выполнения действий
    :param check: некий параметр для проверки наличия разрешения
    :return: функция
    '''
    def do_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            if check in user_permissions:
                func(*args, **kwargs)
            else:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapped_func
    return do_func


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()