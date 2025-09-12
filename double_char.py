while True:
    word = input()
    if word == "End":
        break

    if word == "SoftUni":
        continue

    final = ''.join([chr * 2 for chr in word])
    print(final)
