def check_login_email(string):
    """
    Если result == True, то удовлетворяет
    Если result == False, то не удовлетворяет
    :param string:
    :return: result = {True, False}
    """
    items = ['*', '\\', '|', '/', '-', ',', ':', ';', "'", '@', '&', ')', '(', '{', '}', '[', ']', '=', '?']
    result = True

    for item in items:
        if item in string:
            result = False
            break
    return result

def exit_program(string):
    if string == 'exit':
        return False
    else:
        return True

def registr_func():
    run = True
    
    while run:
        print(" enter your login: ")
        login = input()
        print("enter your email:")
        email = input()
        print("enter your password:")
        password = input()
    
        if email in emails or '@' not in email:
            print("Вы ввели не почту или Уже сущесnвует пользователь с такой почтой")
            if login not in logins:
                if check_login_email(login):
                    pass
            else:
                print("Этот логин уже занят.Введите другой логин")
        else:
            print("Уже сущесnвует пользователь с такой почтой")

def login_func(string):
    run = True

    while run:
        print(" enter your login: ")
        login = input()
        print("enter your password:")
        password = input()

        if login in logins:
            index = logins.index(login)
            if password == passwords[index]:
                print("Вы вошли в систему")
                print(emails[index])
            else:
                print("Логин или пароль неверный")
                print("Хотите повторить[yes] или выйти[exit]?")
                string = input()
                run = exit_program(string)
        else:
            print("Логин или пароль неверный")
            print("Хотите повторить[yes] или выйти[exit]?")
            string = input()
            run = exit_program(string)

    return run  # run == False


if __name__ == '__main__':
    wrong_elements = ['`', '~', '!', '#', '№',  '%', '^', '&', '*', '(',  ')', '-', '_', "'", ',', '?', '"', '|', ';', ':', '+']
    commands = ['L', 'R', 'exit']
    logins = ['dinarayus', "kaseke", "azik"]
    passwords = ["12345", "67890", "qwerty"]
    emails = ["dinara@gmail.com", "kaseke@gmail.com", "azik@gmail.com"]

## сделать запускался терминал, и выводилось приветсвие и команда выход: через ввод q
    run = True

    print("Здраствуйте! Вы вошли в программу")

    while run:

        print("Что вы хотите сделать ?")
        print("(L) Войти")
        print("(R) Зарегистрироваться")
        print("(exit) Выйти")
        string = input()

        if string in commands:
            if string == 'L':
                run = login_func(string)
            elif string == 'R':
                pass
            else:
                run = exit_program('exit')

        else:
            print(f'Command "{string}" not found')
# if "*" or "/" "\ "  "|" "&"  "+" "-" ":" ";"  "," "_"
