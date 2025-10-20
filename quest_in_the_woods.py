days = int(input())
people = int(input())
total_energy = float(input())
water_day = float(input())
food_day = float(input())
energy = True

total_food = food_day * people * days
total_water = water_day * people * days

for day in range(1, days + 1):
    energy_loss = float(input())
    total_energy -= energy_loss

    if total_energy <= 0:
        energy = False
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        total_energy += 0.05 * total_energy
        total_water -= 0.3 * total_water
    if day % 3 == 0:
        total_energy += 0.1 * total_energy
        total_food -= total_food / people

if energy:
    print(f"You are ready for the quest. You will be left with {total_energy:.2f} energy!")

