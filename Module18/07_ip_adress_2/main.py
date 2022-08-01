def IP_int(ip):
    for i in range(len(ip)):
        if not ip[i].isdigit():
            print(ip[i], ' - это не целое число.')
            return False
    return True


def IP_range(ip):
    for i in range(len(ip)):
        if int(ip[i]) > 255:
            print(ip[i],'превышает 255.')
            return False
        elif int(ip[i]) < 0:
            print(ip[i], "меньше 0.")
            return False
    return True

def IP_count_nums(ip):
    if len(ip) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        return False
    return True


IP = input('Введите IP: ').split('.')

if IP_count_nums(IP) and IP_range(IP) and IP_int(IP):
    print('IP-адрес корректен.')
