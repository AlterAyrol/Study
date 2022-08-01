class Property:
    bet = 1
    def __init__(self, worth):
        self.__worth = worth

    def tax(self):
        """
        Расчёт налогов на основе стоимости имущества и ставки
        :param bet: процентная ставка
        :bet: int
        :return:
        """
        return (self.__worth / self.bet)


class Apartment(Property):
    bet = 1000

class Car(Property):
    bet = 200

class CountryHouse(Property):
    bet = 500

def start_buy():
    while True:
        try:
            money = int(input("Кол-во денег у покупателя: "))
            break
        except:
            print("Деньги должны быть указаны в цифрах.")
    while True:
        try:
            price = int(input("Стоимость имущества: "))
            break
        except:
            print("Деньги должны быть указаны в цифрах.")
    while True:
        try:
            choice = int(input("Что будем покупать: 1 - апартаменты, 2 - машину, 3 - загородный дом: "))
            if choice == 1:
                purchase = Apartment(price)
                break
            elif choice == 2:
                purchase = Car(price)
                break
            elif choice == 3:
                purchase = CountryHouse(price)
                break
        except:
            print("Вы сделали неправильный выбор:)")
    cash = money - (price + purchase.tax())
    if cash >= 0:
        print(f"Вы успешно приобрели жильё. "
              f"У вас осталось: {cash} рублей. "
              f"Налог на жильё составляет: {purchase.tax()} рублей")
    else:
        print(f"У вас не хватило {-cash} рублей на покупку.")
    while True:
        go_next = input("Продолжить покупки? (да/нет) ").lower()
        if go_next == "да":
            start_buy()
        elif go_next == 'нет':
            print("Покупки окончены.")
            break
        else:
            print("Неправильно указана команда.")



start_buy()
