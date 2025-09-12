word = input().lower()
counter = 0

if "fish" in word:
    count = word.count("fish")
    counter += count
if "sand" in word:
    count = word.count("sand")
    counter += count
if "water" in word:
    count = word.count("water")
    counter += count
if "sun" in word:
    count = word.count("sun")
    counter += count

print(counter)