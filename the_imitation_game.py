def move(message_, num_):
    moving = message_[:num_]
    message = message_[num_:] + moving
    return message


def insert(message_, index_, value_):
    message = message_[:index_] + value_ + message_[index_:]
    return message


def changeall(message_, substring_, replacement_):
    message = message_.replace(substring_, replacement_)
    return message


message = input()

command = input()
while command != "Decode":

    command = command.split("|")
    action = command[0]

    if action == "Move":
        num = int(command[1])
        message = move(message, num)

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = insert(message, index, value)

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = changeall(message, substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
