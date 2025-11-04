command = input()
while command != "end":
    string = command[::-1]
    print(f"{command} = {string}")
    command = input()