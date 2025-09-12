coffee = 0

while True:
    command = input()
    if command == "END":
        break

    event = command.lower()
    if event not in {"coding", "dog", "cat", "movie"}:
        continue

    if command.isupper():
        coffee += 2
    else:
        coffee += 1

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
