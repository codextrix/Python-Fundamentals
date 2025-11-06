parts = input().split()

total = 0.0

for p in parts:
    first, last = p[0], p[-1]
    num = float(p[1:-1])

    pos_first = ord(first.lower()) - ord('a') + 1
    pos_last = ord(last.lower()) - ord('a') + 1

    if first.isupper():
        num /= pos_first
    else:
        num *= pos_first

    if last.isupper():
        num -= pos_last
    else:
        num += pos_last

    total += num

print(f"{total:.2f}")
