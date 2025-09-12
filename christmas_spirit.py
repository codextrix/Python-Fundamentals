ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15

quantity_of_decorations = int(input())
days_until_Christmas = int(input())

total_spirit = 0
total_cost = 0

for current_day in range(1, days_until_Christmas + 1):

    if current_day % 11 == 0:
        quantity_of_decorations += 2

    if current_day % 2 == 0:
        total_cost += ORNAMENT_SET * quantity_of_decorations
        total_spirit += 5

    if current_day % 3 == 0:
        total_cost += (TREE_SKIRT + TREE_GARLAND) * quantity_of_decorations
        total_spirit += 3 + 10  # 13 total

    if current_day % 5 == 0:
        total_cost += TREE_LIGHTS * quantity_of_decorations
        total_spirit += 17

        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20

        total_cost += TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS

if days_until_Christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
