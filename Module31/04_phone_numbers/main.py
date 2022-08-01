import re


def check(val: str) -> str:
    test1 = re.match(r'[8-9]{1}[0-9]{9}', val)
    if test1 == None:
        return 'не подходит'
    return 'всё в порядке'


numbers = ['9999999999', '999999-999', '99999x9999']

for i, val in enumerate(numbers):
    print(i+1, '-й номер: ', check(val), sep = '')