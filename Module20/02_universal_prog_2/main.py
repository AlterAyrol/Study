def is_prime(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def crypto(text):
    # text = list(text)
    # work_text = []
    # for i, val in enumerate(text):
    #     if is_prime(i):
    #         work_text.append(val)
    # return work_text
    return [val for i, val in enumerate(list(text)) if is_prime(i)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

