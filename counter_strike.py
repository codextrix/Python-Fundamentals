def battle_game(energy):
    won_battle_counter = 0

    while True:
        command = input()

        if command == "End of battle":
            return f"Won battles: {won_battle_counter}. Energy left: {energy}"

        distance = int(command)
        if energy >= distance:
            won_battle_counter += 1
            energy -= distance

            if won_battle_counter % 3 == 0:
                energy += won_battle_counter

        else:
            return f"Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy"


initial_energy = int(input())
result = battle_game(initial_energy)

print(result)


