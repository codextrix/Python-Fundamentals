def make_upper(user_password_, index_):
    before = user_password_[:index_]
    after = user_password_[index_+1:]
    new_letter = user_password_[index_].upper()
    new_password = before + new_letter + after
    return new_password

def make_lower(user_password_, index_):
    before = user_password_[:index_]
    after = user_password_[index_ + 1:]
    new_letter = user_password_[index_].lower()
    new_password = before + new_letter + after
    return new_password

def insert(user_password_, index_,char_):
    if 0 <= index_ <= len(user_password_):
        before = user_password_[:index_]
        after = user_password_[index_:]
        new_password = before + char_ + after
        return new_password
    return None

def replace(user_password_, char_, value_):
    if char in user_password_:
        ascii_char = ord(char_)
        suma = ascii_char + value_
        new_char = chr(suma)
        new_password = user_password_.replace(char_, new_char)
        return new_password
    return None

user_password = input()

command = input()

while command != "Complete":
    command = command.split()
    action = command[0]

    if action == "Make":
        index = int(command[2])
        if 0 <= index < len(user_password):

            if command[1] == "Upper":
                user_password = make_upper(user_password, index)
            elif command[1] == "Lower":
                user_password = make_lower(user_password, index)
            print(user_password)

    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        user_password = insert(user_password, index, char)
        print(user_password)

    elif action == "Replace":
        char = command[1]
        value = int(command[2])
        user_password = replace(user_password,char, value)
        print(user_password)

    elif action == "Validation":
        if len(user_password) < 8:
            print("Password must be at least 8 characters long!")

        if not all(ch.isalnum() or ch == "_" for ch in user_password):
            print("Password must consist only of letters, digits and _!")

        if not any(ch.isupper() for ch in user_password):
            print("Password must consist at least one uppercase letter!")

        if not any(ch.islower() for ch in user_password):
            print("Password must consist at least one lowercase letter!")

        if not any(ch.isdigit() for ch in user_password):
            print("Password must consist at least one digit!")

    command = input()