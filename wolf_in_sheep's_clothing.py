queue = input().split(", ")
animals = list(queue)

animals = animals[::-1]

if animals[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    wolf = animals.index("wolf")
    print(f"Oi! Sheep number {wolf}! You are about to be eaten by a wolf!")