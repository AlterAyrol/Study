def detail_exists(detail, detail_in_stock):
        for i_det in range(len(detail_in_stock)):
                 if detail_in_stock[i_det][0] == detail:
                        return True
        return False

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_request = input("Введите название нужной детали: ")
detail_count = 0
detail_cost = 0

if detail_exists(detail_request, shop):
        for i_det in range(len(shop)):
                if detail_request == shop[i_det][0]:
                        detail_count += 1
                        detail_cost += shop[i_det][1]
        print('Кол-во деталей —', detail_count)
        print('Общая стоимость —', detail_cost)

else:
        print("Такой детали нет в магазине!")