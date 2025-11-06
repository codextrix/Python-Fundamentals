s = input()

power = 0
result = []

for i, ch in enumerate(s):
    if ch == '>':
        result.append('>')

        if i + 1 < len(s) and s[i + 1].isdigit():
            power += int(s[i + 1])
    else:
        if power > 0:
            power -= 1
        else:
            result.append(ch)

print(''.join(result))
