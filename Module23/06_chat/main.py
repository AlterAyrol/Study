def history():
    try:
        with open('history.txt', 'r') as history_file:
            for i in history_file:
                print(i, end = '')
    except FileNotFoundError:
        print("История чата пуста")

def send_message(user):
    with open('history.txt', 'a') as history_file:
        text = input('Введите текст сообщения: ')
        text = user + ': ' + text + '\n'
        history_file.write(text)


user_name = input("Введите ваше имя: ")
try:
    while True:
        command = int(input('\nВведите комманду:\n1). Посмотреть текущий текст чата.\n2). Отправить сообщение\n'))
        if command == 1:
            history()
        elif command == 2:
            send_message(user_name)
        else:
            raise AttributeError
except AttributeError:
    print("Неправильно введена команда. Работа программы прекращена.")

