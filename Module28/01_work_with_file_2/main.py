class File:
    """
    Класс, который пробует открыть нужный файл для записи в него данных. При отсутствии такого файла,
    класс создаёт его в режиме записи.
    """
    def __init__(self, enter_file: str, operation: str) -> None:
        print('Start work')
        self.enter_file = enter_file
        self.operation = operation

    def __enter__(self):
        #а что возвращает эта функция?
        try:
            file = open(self.enter_file, self.operation)
            return file
        except FileNotFoundError:
            file = open(self.enter_file, 'w')
            return file
        except:
            print('something wrong')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # и что возвращает эта функция?
        try:
            file.close()
        finally:
            return True


with File('example.txt', 'r') as file:
    file.write('Hi All')