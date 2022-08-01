def count_elem(elem):
    return elem[1]

analysis = open('analysis.txt', 'w')
analysis.close()

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'

with open('text.txt', 'w') as start_file:
    text = 'Mama myla ramu.'
    start_file.write(text)

analysis_dict = {}

with open('text.txt', 'r') as start_file:
    for i_len in start_file:
        words_list = i_len.split()
        for i_word_list, val_word_list in enumerate(words_list):
            letter_list = list(val_word_list)
            for i_letter in letter_list:
                if str(i_letter).lower() in analysis_dict:
                    analysis_dict[str(i_letter).lower()] += 1
                elif str(i_letter).lower() in alphabet_lower:
                    analysis_dict[str(i_letter).lower()] = 1

analysis_dict_count = sum(analysis_dict.values())
for i_key, i_val in analysis_dict.items():
    analysis_dict[i_key] = round(i_val / analysis_dict_count, 3)


analysis_list = [[i_key, i_val] for i_key, i_val in analysis_dict.items()]
analysis_list.sort(key = count_elem, reverse=True)
for i_val in range(len(analysis_list) - 1):
    if analysis_list[i_val][1] == analysis_list[i_val + 1][1]:
        if alphabet_lower.index(analysis_list[i_val][0]) > alphabet_lower.index(analysis_list[i_val + 1][0]):
            analysis_list[i_val][0], analysis_list[i_val+1][0] = analysis_list[i_val+1][0], analysis_list[i_val][0]

with open('analysis.txt', 'a') as analysis:
    for i in range(len(analysis_list)):
        text = f'{analysis_list[i][0]} {analysis_list[i][1]}\n'
        analysis.write(text)


with open('analysis.txt', 'r') as analysis:
    for i in analysis:
        print(i, end='')
