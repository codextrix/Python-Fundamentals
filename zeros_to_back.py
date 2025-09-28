list_as_strings = input().split(", ")
list_as_integer = [int(number) for number in list_as_strings]

for element in range(list_as_integer.count(0)):
    list_as_integer.remove(0)
    list_as_integer.append(0)

print(list_as_integer)