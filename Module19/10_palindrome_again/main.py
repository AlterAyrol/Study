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

text = input('Введите строку: ')

histogram = text_dict(text)

invert_histogram = invert_hist(histogram)

count = 0
for i in sorted(invert_histogram):
    if i % 2 != 0:
        count += len(invert_histogram[i])
if count > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
