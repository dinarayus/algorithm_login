def check_login_email(string):
    """
    Если result == True, то удовлетворяет
    Если result == False, то не удовлетворяет
    :param string:
    :return: result = {True, False}
    """
    items = ['*', '\\', '|', '/', '-', ',', ':', '_', ';', "'", '@', '&', ')', '(', '{', '}', '[', ']', '=', '?']
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


def registr_func(string):
    run1 = True
    
    while run1:
        print(" enter your login: ")
        login = input()
        print("enter your email:")
        email = input()
        print("enter your password:")
        password = input()
    
        if email not in emails and '@' in email:
            if login not in logins:
                if check_login_email(login):
                    index = email.index('@')
                    if check_login_email(email[:index] + email[index+1:]):
                        logins.append(login)
                        passwords.append(password)
                        emails.append(email)
                        print('You have successfully registered!')
                        run1 = False
                    else:
                        print(' the wrong mail format')
                else:
                    print('the wrong login format')
            else:
                print("this login is already taken. Enter another mail.")
        else:
            print("this email already belongs to the account")
    return True

def login_func(string):
    run1 = True

    while run1:
        print(" enter your login: ")
        login = input()
        print("enter your password:")
        password = input()

        if login in logins:
            index = logins.index(login)
            if password == passwords[index]:
                print("you're logged in")
                print(emails[index])
                print("want to exit[exit]?")
                string = input()
                run1 = exit_program(string)

            else:
                print("Username or password is incorrect")
                print("want to try again[yes] or exit[exit]?")
                string = input()
                run1 = exit_program(string)
        else:
            print("Username or password is incorrect")
            print("want to try again[yes] or exit[exit]?")
            string = input()
            run1 = exit_program(string)

    return True  # run == False


if __name__ == '__main__':
  #  wrong_elements = ['`', '~', '!', '#', '№',  '%', '^', '&', '*', '(',  ')', '-', '_', "'", ',', '?', '"', '|', ';', ':', '+']
    commands = ['L', 'R', 'exit']
    logins = ['dinarayus', "kaseke", "azik"]
    passwords = ["12345", "67890", "qwerty"]
    emails = ["dinara@gmail.com", "kaseke@gmail.com", "azik@gmail.com"]

## сделать запускался терминал, и выводилось приветсвие и команда выход: через ввод q
    run = True

    print("Hello! You have entered the program")

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
                run = registr_func(string)

            else:
                run = exit_program('exit')

        else:
            print(f'Command "{string}" not found')
# if "*" or "/" "\ "  "|" "&"  "+" "-" ":" ";"  "," "_"
