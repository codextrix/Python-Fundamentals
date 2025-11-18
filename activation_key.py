def contains(activation_key_:str,command_:list)->str:
    substring = command_[1]
    if substring in activation_key_:
        return f"{activation_key_} contains {substring}"
    return "Substring not found!"
def flip(activation_key_:str,command_:list)->str:
    upper_lower = command[1]
    start = int(command[2])
    end = int(command[3])
    before_substring = activation_key_[:start]
    after_substring = activation_key_[end:]
    substring = activation_key_[start:end]
    if upper_lower == "Upper":
        substring = substring.upper()
    elif upper_lower == "Lower":
        substring = substring.lower()

    activation_key_ = before_substring + substring + after_substring
    return activation_key_
def slice(activation_key_:str,command_:list)->str:
    start = int(command[1])
    end = int(command[2])
    before_deleting = activation_key_[:start]
    after_deleting = activation_key_[end:]
    activation_key_ = before_deleting + after_deleting
    return activation_key_

activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")

    action = command[0]

    if action == "Contains":
        print(contains(activation_key,command))
    elif action == "Flip":
        activation_key = flip(activation_key,command)
        print(activation_key)
    elif action == "Slice":
        activation_key = slice(activation_key, command)
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")