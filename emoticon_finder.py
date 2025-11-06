string = input()

for ch in range(len(string) -1):
    if string[ch] == ":":
        print(f":{string[ch + 1]}")

