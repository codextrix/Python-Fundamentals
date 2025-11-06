string = input()
valid = []
for ch in string:
    if not valid or ch != valid[-1]:
        valid.append(ch)

print("".join(valid))