import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

product = []

def easy_syte(count, stop_count = 0):
    if count == stop_count:
        return
    product.append(input('Введите название продукта для нового сайта: '))
    site_copy = copy.deepcopy(site)
    for i, val in enumerate(product):
        site_copy['html']['head']['title'] = f'Куплю/продам {product[i]} недорого'
        site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {product[i]}'
        print(site_copy)
    easy_syte(count, stop_count + 1)


easy_syte(int(input('Сколько сайтов: ')))
