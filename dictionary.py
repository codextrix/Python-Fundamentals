words_definition = input()
words = words_definition.split(" | ")

dictionary = {}

for word in words:
    w, definition = word.split(": ")
    if w in dictionary:
        dictionary[w].append(definition)
    else:
        dictionary[w] = []
        dictionary[w].append(definition)


test_words = input().split(" | ")

command = input()
if command == "Test":
    for test_word in test_words:
        if test_word in dictionary:
            print(f"{test_word}:")
            for definition in dictionary[test_word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for thing in dictionary:
        print(thing,end=" ")