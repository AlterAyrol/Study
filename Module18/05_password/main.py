def good_len(pas):
    if len(pas) >= 8:
        return True
    print('Пароль должен состоять хотя бы из восьми символов!')
    return False

def upper_sym(pas):
    if not pas.islower():
        return True
    print('Должна быть хотя бы одна заглавная буква!')
    return False

def num_in_pass(pas):
    nums = '0123456789'
    count = 0
    for sym in pas:
        if sym in nums:
            count += 1
    if count >= 3:
        return True
    else:
        print("Должно быть хотя бы три цифры!")
        return False

while True:
    password = input('Придумайте пароль: ')

    if good_len(password) and upper_sym(password) and num_in_pass(password):
        break


print('Это надёжный пароль!')

