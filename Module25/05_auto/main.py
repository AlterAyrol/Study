class Car:
    def __init__(self, x, y, way_angle, distance = 0, speed = 50, hours = 3):
        self.__x = x
        self.__y = y
        self.__way_angle = way_angle
        self.__distance = distance
        self.__speed = speed
        self.__hours = hours

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_way_angle(self):
        return self.__way_angle
    def get_distance(self):
        return self.__distance
    def get_speed(self):
        return self.__speed
    def get_hours(self):
        return self.__hours

    def set_x(self, num):
        self.__x = num
    def set_y(self, num):
        self.__y = num
    def set_way_angle(self, num):
        self.__way_angle = num
    def set_distance(self, num):
        self.__distance += num

    def traveled_distance(self):
        traveled = self.get_speed() * self.get_hours()
        self.set_distance(traveled)
        return f"Сейчас проехали {traveled} километров. Всего проехали {self.get_distance()} километров"

class Bus(Car):
    def __init__(self, x, y, way_angle, passengers, money = 0, distance = 0, speed = 50, hours = 3):
        super().__init__(x, y, way_angle, distance = 0, speed = 50, hours = 3)
        self.__passengers = passengers
        self.__money = money

    def get_passengers(self):
        return self.__passengers
    def get_money(self):
        return self.__money

    def set_passengers(self, num):
        self.__passengers += num
    def set_money(self, num):
        self.__money += num

    def enter(self, num):
        self.set_passengers(num)
        return f"Вошло {num} пассажиров. Всего в салоне автобуса {self.get_passengers()} пассажиров."
    def exit(self, num):
        self.set_passengers(-num)
        return f"Вышло {num} пассажиров. Всего в салоне автобуса {self.get_passengers()} пассажиров."

    def traveled_distance(self):
        super().traveled_distance()
        money_for_each_km = 2
        traveled = self.get_speed() * self.get_hours()
        money_for_trip = traveled * self.get_passengers() * money_for_each_km
        self.set_money(money_for_trip)
        return f"За время поездки заработано {self.get_money()} рублей."


car1 = Car(x=1,y=3, way_angle=5)
print(car1.traveled_distance())
bus1 = Bus(x=1,y=3, way_angle=5,passengers=5)
print(bus1.traveled_distance())

