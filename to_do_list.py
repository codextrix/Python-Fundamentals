note = [0] * 10

while True:
    notes = input()
    if notes == "End":
        break
    tokens = notes.split("-")
    importance = int(tokens[0]) - 1
    message = tokens[1]
    note.pop(importance)
    note.insert(importance, message)

result = [element for element in note if element != 0]
print(result)