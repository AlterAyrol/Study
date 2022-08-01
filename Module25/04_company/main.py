class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_age(self):
        return self.__age
    def set_name(self, new_name):
        self.__name = new_name
    def set_surname(self, new_surname):
        self.__surname = new_surname
    def set_age(self, new_age):
        self.__age = new_age

class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
    def salary(self):
        return None

class Manager(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
    def salary(self):
        return 13000
    def __str__(self):
        return '\nМенеджер\n'+ "Фамилия: " + self.get_surname() + " Имя: " + self.get_name() +\
               " Зарплата: " + str(self.salary())

class Agent(Person):
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.__sales_volume = sales_volume
    def get_sales_volume(self):
        return self.__sales_volume
    def salary(self):
        return 5000 + (self.get_sales_volume() // 100 * 5)
    def __str__(self):
        return '\nАгент\n'+ "Фамилия: " + self.get_surname() + " Имя: " + self.get_name() +\
               " Зарплата: " + str(self.salary())


class Worker(Person):
    def __init__(self, name, surname, age, work_hours):
        super().__init__(name, surname, age)
        self.__work_hours = work_hours
    def get_work_hours(self):
        return self.__work_hours
    def salary(self):
        return 100 * self.__work_hours
    def __str__(self):
        return '\nРабочий\n'+ "Фамилия: " + self.get_surname() + " Имя: " + self.get_name() +\
               " Зарплата: " + str(self.salary())


manager1= Manager(name='Первый', surname='Менеджер', age=20)
manager2= Manager(name='Второй', surname='Менеджер', age=25)
manager3= Manager(name='Третий', surname='Менеджер', age=30)
agent1 = Agent(name='Первый', surname='Агент', age=21, sales_volume=2000)
agent2 = Agent(name='Второй', surname='Агент', age=26, sales_volume=4500)
agent3 = Agent(name='Третий', surname='Агент', age=31, sales_volume=7000)
worker1= Worker(name='Первый', surname='Рабочий', age=22, work_hours=35)
worker2= Worker(name='Второй', surname='Рабочий', age=27, work_hours=40)
worker3= Worker(name='Третий', surname='Рабочий', age=32, work_hours=45)
print(manager1)
print(manager2)
print(manager3)
print(agent1)
print(agent2)
print(agent3)
print(worker1)
print(worker2)
print(worker3)
