def letters(us_wanted_, upper_lower_):
    if upper_lower_ == "Upper":
        return us_wanted_.upper()
    else:
        return us_wanted_.lower()


def reverse(us_wanted_, start_index_, end_index_):

    if 0 <= start_index_ <= end_index_ < len(us_wanted_):
        substring = us_wanted_[start_index_:end_index_ + 1]
        return substring[::-1]
    return None


def substrings(us_wanted_, substring_):
    if substring_ in us_wanted_:
        us_wanted_ = us_wanted_.replace(substring_, "", 1)
        print(us_wanted_)
        return us_wanted_
    else:
        print(f"The username {us_wanted_} doesn't contain {substring_}.")
        return us_wanted_


def replace_char(us_wanted_, char_):
    us_wanted_ = us_wanted_.replace(char_, "-")
    print(us_wanted_)
    return us_wanted_


def is_valid(us_wanted_, char_):
    if char_ in us_wanted_:
        print("Valid username.")
    else:
        print(f"{char_} must be contained in your username.")


us_wanted = input()

command = input()
while command != "Registration":
    parts = command.split()

    if parts[0] == "Letters":
        upper_lower = parts[1]
        us_wanted = letters(us_wanted, upper_lower)
        print(us_wanted)

    elif parts[0] == "Reverse":
        start_index = int(parts[1])
        end_index = int(parts[2])
        result = reverse(us_wanted, start_index, end_index)
        if result is not None:
            print(result)

    elif parts[0] == "Substring":
        substring = parts[1]
        us_wanted = substrings(us_wanted, substring)

    elif parts[0] == "Replace":
        ch = parts[1]
        us_wanted = replace_char(us_wanted, ch)

    elif parts[0] == "IsValid":
        ch = parts[1]
        is_valid(us_wanted, ch)

    command = input()
