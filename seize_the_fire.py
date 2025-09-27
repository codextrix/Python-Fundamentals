fire_cells = input().split("#")
water = int(input())

valid_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

put_out_cells = []
effort = 0.0
total_fire = 0

for chunk in fire_cells:
    fire_type, value_str = [p.strip() for p in chunk.split(" = ")]
    value = int(value_str)

    if fire_type in valid_ranges and value in valid_ranges[fire_type] and water >= value:
        water -= value
        put_out_cells.append(value)
        effort += value * 0.25
        total_fire += value

print("Cells:")
for v in put_out_cells:
    print(f"- {v}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")