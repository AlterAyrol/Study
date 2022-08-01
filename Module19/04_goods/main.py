def quantity_price(key):
    count = 0
    cost = 0
    for i in range(len(store[key])):
        count += store[key][i]['quantity']
        cost += store[key][i]['quantity'] * store[key][i]['price']
    return count, cost

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

goods_keys = list(goods.keys())

for i_keys in range(len(goods_keys)):
    i_quantity, i_price = quantity_price(goods[goods_keys[i_keys]])
    print(goods_keys[i_keys], '-', i_quantity, 'штук, стоимость', i_price, 'рубля')
