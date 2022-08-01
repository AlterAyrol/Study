import random

class All:
    def __init__(self, name, fullness = 30):
        self.__name = name
        self.__fullness = 30
    def get_name(self):
        return self.__name
    def get_fullness(self):
        return self.__fullness
    def set_fullness(self, num):
        self.__fullness += num



class Husband(All):
    fullness = 30
    def __init__(self, name, fullness = 30):
        All.__init__(self, name, fullness)
        self.__happiness = 100
    def __str__(self):
        return f'Муж с именем: {self.get_name}. Сытостью: {self.get_fullness()}. ' \
               f'Степенью счастья: {self.get_happiness()}'
    def get_happiness(self):
        return self.__happiness
    def set_happiness(self, num):
        self.__happiness += num



class Wife(All):
    def __init__(self, name, fullness = 30):
        All.__init__(self, name, fullness)
        self.__happiness = 100
        self.__coat = 0
    def __str__(self):
        return f'Жена с именем: {self.get_name()}. Сытостью: {self.get_fullness()}.' \
               f' Степенью счастья: {self.get_happiness()}'
    def get_happiness(self):
        return self.__happiness
    def set_happiness(self, num):
        self.__happiness += num
    def get_coat_count(self):
        return self.__coat
    def set_coat_count(self, num):
        self.__coat += num


class Cat(All):
    def __str__(self):
        return f'Кот с кличкой: {self.get_name()}. Сытость кота: {self.get_fullness()}'


class House:
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__dirt = 0
        wife_name = input("Введите, как зовут жену: ")
        husband_name = input("Введите, как зовут мужа: ")
        cat_name = input("Введите, как зовут кота: ")
        self.wife = Wife(wife_name)
        self.husband = Husband(husband_name)
        self.cat = Cat(cat_name)
        self.__money_for_year = 0
        self.__food_for_year = 0
    def get_money(self):
        return self.__money
    def set_money(self, num):
        self.__money += num
    def get_food(self):
        return self.__food
    def set_food(self, num):
        self.__food += num
    def get_cat_food(self):
        return self.__cat_food
    def set_cat_food(self, num):
        self.__cat_food += num
    def get_dirt(self):
        return self.__dirt
    def set_dirt(self, num):
        self.__dirt += num
    def get_money_for_year(self):
        return self.__money_for_year
    def set_money_for_year(self, num):
        self.__money_for_year += num
    def get_food_for_year(self):
        return self.__food_for_year
    def set_food_for_year(self, num):
        self.__food_for_year += num
    def buy_foodstuff(self):
        if self.get_money() >= 150:
            self.set_food(120)
            self.set_cat_food(30)
            self.set_money(-150)
            print('Жена сходила в магазин и купила продуктов (еда +120, еда для кота + 30)')
    def coat(self):
        self.wife.set_happiness(60)
        self.set_money(-350)
        self.wife.set_coat_count(1)
        self.wife.set_fullness(-10)
        print(f'Жена купила шубу (счастье +60(всего - {self.wife.get_happiness()}),'
              f'деньги - 350(всего - {self.get_money()}))')
    def clean_house(self):
        if self.get_dirt() >= 100:
            self.set_dirt(-100)
        else:
            self.set_dirt(-self.get_dirt())
        self.wife.set_fullness(-10)
        print(f"Жена убралась дома (уровень грязи в доме - {self.get_dirt()})")
    def work(self):
        self.set_money(150)
        self.set_money_for_year(150)
        self.husband.set_fullness(-10)
        print(f"Муж пришёл с работы и принёс 150р. (всего денег - {self.get_money()})")
    def game(self):
        self.husband.set_happiness(20)
        self.husband.set_fullness(-10)
        print(f"Муж поиграл (счастье +20(всего - {self.husband.get_happiness()})).")
    def husband_eat(self):
        if self.get_food() >= 30:
            self.husband.set_fullness(30)
            self.set_food(-30)
            self.set_food_for_year(30)
            print(f"Муж поел (сытость - {self.husband.get_fullness()}, еды осталось - {self.get_food()})")
        else:
            self.husband.set_fullness(self.get_food())
            self.set_food(-self.get_food())
            self.set_food_for_year(-self.get_food())
            print(f"Муж поел (сытость - {self.husband.get_fullness()}, еды осталось - {self.get_food()})")
    def wife_eat(self):
        if self.get_food() >= 30:
            self.wife.set_fullness(30)
            self.set_food(-30)
            self.set_food_for_year(30)
            print(f"Муж поел (сытость - {self.wife.get_fullness()}, еды осталось - {self.get_food()})")
        else:
            self.wife.set_fullness(self.get_food())
            self.set_food(-self.get_food())
            self.set_food_for_year(-self.get_food())
            print(f"Муж поел (сытость - {self.wife.get_fullness()}, еды осталось - {self.get_food()})")
    def cat_eat(self):
        self.cat.set_fullness(20)
        self.set_cat_food(-10)
        print(f"Кот {self.cat.get_name()} поел (сытость - {self.cat.get_fullness()}, "
              f"еды осталось - {self.get_cat_food()})")
    def tear_wallpaper(self):
        self.set_dirt(5)
        print(f"Кот {self.cat.get_name()} дерёт обои! (уровень грязи - {self.get_dirt()})")
    def cat_sleep(self):
        print('Кот проспал весь день.')
    def too_much_dirt(self):
        if self.get_dirt() > 90:
            self.wife.set_happiness(-10)
            self.husband.set_happiness(-10)
            print(f"Дома слишком грязно! (уровень грязи - {self.get_dirt()})")
    def every_day_dirt(self):
        self.set_dirt(5)
        print(f'Прошёл день, пришла грязь (уровень грязи в доме увеличился на 5 (всего - {self.get_dirt()}))')


def one_year_live():
    day = 1
    family1 = House()
    while day <= 364:
        print(f"Наступил {day}-й день.", sep='')
        cat_choice = random.randint(0, 1)
        if family1.husband.get_fullness() < 30:
            family1.husband_eat()
        elif family1.husband.get_happiness() < 20:
            family1.game()
        else:
            family1.work()

        if family1.wife.get_fullness() < 30:
            family1.wife_eat()
        elif family1.wife.get_happiness() < 20:
            family1.coat()
        elif family1.get_dirt() > 85:
            family1.clean_house()
        elif family1.get_food() < 70:
            family1.buy_foodstuff()
        elif family1.get_money() > 500:
            family1.coat()

        if family1.cat.get_fullness() < 20:
            family1.cat_eat()
        elif cat_choice == 0:
            family1.tear_wallpaper()
        else:
            family1.cat_sleep()

        family1.too_much_dirt()
        family1.every_day_dirt()
        day += 1
        print()

    print(f'Прошёл год. Итого:\nЗаработано денег за год: {family1.get_money_for_year()}'
          f'\nЕды съедено за год: {family1.get_food_for_year()}'
          f'\nШуб куплено за год: {family1.wife.get_coat_count()}')



one_year_live()