def password():
    while True:
        password_len = input("Enter a password: ")
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if len(password_len) <5:
            print("Please enter more then 5 letter's")
        elif not len(password_len)<=16:
            print("Please enter less then 16 letter's")
        elif not any(char.isdigit() for char in password_len):
            print("Please enter the number in it")
        elif not any(char in special_characters for char in password_len):
            print("Please enter the Special Character in it")
        elif not any(char.isupper() for char in password_len):
            print("Please enter the Capital letter in it")
        elif not any(char.islower() for char in password_len):
            print("Please enter the Small letter in it")
        else:
            print("Password is matched")
            break
password()
