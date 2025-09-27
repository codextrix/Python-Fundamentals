gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break

    command_split = command.split(" ")
    action = command_split[0]

    if action == "OutOfStock":
        gift = command_split[1]
        for element in range(len(gifts)):
            if gifts[element] == gift:
                gifts[element] = "None"
    elif action == "Required":
        gift = command_split[1]
        index = int(command_split[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = command_split[1]
        gifts[-1] = gift

result = []

for g in gifts:
    if g != "None":
        result.append(g)

print(" ".join(result))