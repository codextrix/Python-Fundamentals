num_lines = int(input())
tank_capacity = 255
for line in range(num_lines):
    liters_water = int(input())
    if tank_capacity < liters_water:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_water

print(255 - tank_capacity)