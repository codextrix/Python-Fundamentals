s = input()

i = 0
n = len(s)
pieces = []
unique = set()

while i < n:

    start = i
    while i < n and not s[i].isdigit():
        i += 1
    chunk = s[start:i].upper()

    start = i
    while i < n and s[i].isdigit():
        i += 1
    count = int(s[start:i])

    if count > 0:
        pieces.append(chunk * count)
        unique.update(chunk)

result = ''.join(pieces)
print(f"Unique symbols used: {len(unique)}")
print(result)
