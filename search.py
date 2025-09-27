n = int(input())
word = input()

strings = []
filtered = []

for _ in range(n):
    current_sting = input()
    strings.append(current_sting)

for _string in strings:
    if word in _string:
        filtered.append(_string)

print(strings)
print(filtered)