concealed_message = input()

command = input()
while command != "Reveal":
    command = command.split(":|:")
    action = command[0]

    if action == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            concealed_message += reversed_substring
            print(concealed_message)
        else:
            print("error")

    elif action == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")
