site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_key(struct, key, max_deep = 0, deep = 1):
    if deep == max_deep:
        if key in struct:
            return struct[key]
        else:
            return None
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_deep, deep + 1)
            if result:
                break
        else:
            result = None
    return result


new_key = input('Введите искомый ключ:  ')
need_deep = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if need_deep == 'n':
    value = find_key(site, new_key)
    if value:
        print(f'Значение ключа:- {new_key} имеет значения:', value)
    else:
        print('Нет такого имени(с)')
elif need_deep == 'y':
    value = find_key(site, new_key, int(input('Введите максимальную глубину: ')))
    if value:
        print(f'Значение ключа:- {new_key} имеет значения:', value)
    else:
        print('Нет такого имени(с)')
else:
    print("Ошибка ввода")

