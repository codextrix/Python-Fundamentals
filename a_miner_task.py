words = {}
something = input()
while something != "stop":
    quantity = int(input())

    if something not in words.keys():
        words[something] = 0

    words[something] += quantity
    something = input()
for key, value in words.items():
    print(f"{key} -> {value}")
