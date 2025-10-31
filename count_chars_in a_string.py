characters = input()
letters = {}
for element in characters:
    if element == " ":
        continue
    if element not in letters.keys():
        letters[element] = 0
    letters[element] += 1
for character, ocurrence in letters.items():
    print(f"{character} -> {ocurrence}")
