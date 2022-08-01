alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('text.txt', 'w') as start_file:
    start_file.write('Hello\n' * 4)

with open('text.txt', 'r') as start_file:
    with open('cipher_text.txt', 'w') as code_file:
        for i_start_len, val_start_len in enumerate(start_file):
            shift = 1 + i_start_len
            work_word = []
            letter = list(val_start_len)
            for i_letter, val_letter in enumerate(letter):
                if val_letter in alphabet_lower:
                    number = alphabet_lower.index(val_letter)
                    number += shift
                    letter[i_letter] = alphabet_lower[number]
                elif val_letter in alphabet_upper:
                    number = alphabet_upper.index(val_letter)
                    number += shift
                    letter[i_letter] = alphabet_upper[number]
            letter = ''.join(letter)
            code_file.write(str(letter))

with open('cipher_text.txt', 'r') as code_file:
    for i in code_file:
        print(i, end = '')
