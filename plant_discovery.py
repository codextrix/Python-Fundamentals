n = int(input())
plants_dictionairy = {}

for _ in range(n):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])

    if plant not in plants_dictionairy:
        plants_dictionairy[plant] = {"rarity": rarity, "ratings": []}
    else:
        plants_dictionairy[plant]["rarity"] = rarity

command = input()

while command != "Exhibition":
    action, data = command.split(": ")

    if action == "Rate":
        plant_name, rating = data.split(" - ")
        rating = float(rating)
        if plant_name in plants_dictionairy:
            plants_dictionairy[plant_name]["ratings"].append(rating)
        else:
            print("error")

    elif action == "Update":
        plant_name, new_rarity = data.split(" - ")
        new_rarity = int(new_rarity)
        if plant_name in plants_dictionairy:
            plants_dictionairy[plant_name]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        plant_name = data
        if plant_name in plants_dictionairy:
            plants_dictionairy[plant_name]["ratings"].clear()
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")


def average(lst):
    return sum(lst) / len(lst) if lst else 0


for plant, info in plants_dictionairy.items():
    avg_rate = average(info["ratings"])
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {avg_rate:.2f}")
