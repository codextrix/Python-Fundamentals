inp = input().split()
inventory = {}

for i in range(0, len(inp), 2):
    food = inp[i]
    quantity = int(inp[i + 1])
    inventory[food] = quantity

print(inventory)