words = input().split()
new_words = [word for word in words if len(word) % 2 == 0]

for w in new_words:
    print(w)