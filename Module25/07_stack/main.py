def text_split(text):
    text = text.split(',')
    return text[0], text[1]

class LIFO_stack:
    def __init__(self):
        self.__stack = []

    def get_stack(self):
        return self.__stack

    def set_stack(self, new_element):
        self.__stack.append(new_element)

class TaskManager:
    def __init__(self):
        self.__LIFO = LIFO_stack()

    def get_LIFO(self):
        return self.__LIFO.get_stack()

    def new_task(self, text, priority):
        self.__LIFO.set_stack([text, priority])

    def sort_manager(self):
        LIFO_dict = {}
        for i_text, i_priority in self.get_LIFO():
            if i_priority in LIFO_dict.keys():
                LIFO_dict[i_priority] += '; '
                LIFO_dict[i_priority] += i_text
            else:
                LIFO_dict[i_priority] = i_text
        keys = sorted(LIFO_dict.keys())
        return LIFO_dict, keys

    def __str__(self):
        work_dict, work_keys = self.sort_manager()
        text = ''
        for i in work_keys:
            text += str(i) + work_dict[i] + '\n'
        return text

    def all(self):
        for i_text, i_priority in self.get_LIFO():
            print(i_priority, i_text)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
# manager.all()
print(manager)
