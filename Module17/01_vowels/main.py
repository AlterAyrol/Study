def vowel_sym(sym):
    if sym == "а" or sym == "я" or sym == "у" or sym == "ю" or sym == "о" or sym == "ё" or sym == "ы" or sym == "и" or sym == "э" or sym == "е":
        return True
    return False


text = input('Введите текст: ')
text_vowel_list = [x for x in text if vowel_sym(x)]

print('Список гласных букв:', text_vowel_list)
print('Длина списка:', len(text_vowel_list))

