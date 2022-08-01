import zipfile

def count_elem(elem):
    return elem[1]

alphabeet_eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabeet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

analysis_dict = {}

with zipfile.ZipFile('voyna-i-mir.zip') as voyna_i_mir_zip:
    voyna_i_mir_zip.extractall()

with open('voyna-i-mir.txt', mode = 'r', encoding = 'utf-8') as voyna_i_mir:
    for i_len in voyna_i_mir:
        words_list = i_len.split()
        for i_word_list, val_word_list in enumerate(words_list):
            letter_list = list(val_word_list)
            for i_letter in letter_list:
                if i_letter in analysis_dict:
                    analysis_dict[i_letter] += 1
                elif i_letter in alphabeet_eng or i_letter in alphabeet_ru:
                    analysis_dict[i_letter] = 1

analysis_list = [[i_key, i_val] for i_key, i_val in analysis_dict.items()]
analysis_list.sort(key = count_elem, reverse=True)

for i in analysis_list:
    print(i)

