from typing import Any


class Date:
    '''
    Класс конвертирующий строку даты в объект класса Date
    '''
    def __init__(self, *args: Any) -> None:
        self.args = args

    @classmethod
    def from_string(cls, string: str) -> str:
        string_list = string.split('-')
        return f'День: {string_list[0]}	Месяц: {string_list[1]}		Год: {string_list[2]}'

    @classmethod
    def is_date_valid(cls, string: str) -> bool:
        string_list = string.split('-')
        return (0 < int(string_list[0]) <= 31) and (0 < int(string_list[1]) <= 12)






date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))