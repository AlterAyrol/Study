def text_dict(words):
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

def invert_hist(hist):
    work_hist_items = list(hist.items())
    work_hist_dict = {}
    for i in range(len(work_hist_items)):
        if work_hist_items[i][1] in work_hist_dict:
            work_hist_dict[work_hist_items[i][1]].append(work_hist_items[i][0])
        else:
            work_hist_dict[work_hist_items[i][1]] = [work_hist_items[i][0]]
    return work_hist_dict

text = input('Введите текст: ')

histogram = text_dict(text)

print('Оригинальный словарь частот:')
for i in sorted(histogram.keys()):
    print(i, ':', histogram[i])

invert_histogram = invert_hist(histogram)

print('Инвертированный словарь частот:')
for i in sorted(invert_histogram.keys()):
    print(i, ':', invert_histogram[i])




