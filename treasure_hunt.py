def loot(inhalt: list, things: list) -> list:
    for item in things:
        if item not in inhalt:
            inhalt.insert(0, item)
    return inhalt


def drop(inhalt: list, current_index: int) -> list:
    if current_index in range(len(inhalt)):
        inhalt.append(inhalt.pop(current_index))
    return inhalt


def steal(inhalt: list, current_count: int) -> list:
    if current_count >= len(inhalt):
        print(", ".join(inhalt))
        inhalt = []
    else:
        stealing_index = len(inhalt) - current_count
        print(", ".join(inhalt[stealing_index:]))
        inhalt = inhalt[:stealing_index]
        return inhalt


treasure_inhalt = input().split("|")
command = input().split()
while True:
    if command[0] == "Yohoho!":
        break

    action = command[0]

    if action == "Loot":
        items = command[1:]
        treasure_inhalt = loot(treasure_inhalt,items)
    elif action == "Drop":
        index = int(command[1])
        treasure_inhalt = drop(treasure_inhalt, index)
    elif action == "Steal":
        count = int(command[1])
        treasure_inhalt = steal(treasure_inhalt, count)
    command = input().split()
if not treasure_inhalt:
    print("Failed treasure hunt.")
else:
    average = sum(len(element) for element in treasure_inhalt) / len(treasure_inhalt)
    print(f"Average treasure gain: {average:.2f} pirate credits.")