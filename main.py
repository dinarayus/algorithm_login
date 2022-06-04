
def exit_program(string):
    if string == 'exit':
        return False
    else:
        return True

def registr_func():
    pass

def login_func():
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
            return exit_program(string)
    else:
        print("Логин или пароль неверный")
        print("Хотите повторить[yes] или выйти[exit]?")
        string = input()
        return exit_program(string)


if __name__ == '__main__':

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
                run = login_func()
            elif string == 'R':
                pass
            else:
                run = exit_program('exit')

        else:
            print(f'Command "{string}" not found')
# if "*" or "/" "\ "  "|" "&"  "+" "-" ":" ";"  "," "_"
