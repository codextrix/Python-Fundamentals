word = input()

indexes = []

for i, ch in enumerate(word):
    if ch.isupper():
        indexes.append(i)
print(indexes)