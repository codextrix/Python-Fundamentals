lst = ['example', 1, 3.14, []]

for i in range(len(lst)):
    print(i, "-",lst[i])


number = list(range(1, 11))
print(number)

string = "a b c d"
list = string.split(" ")
print(list)


listche = ["a", "b"]
print("-".join(listche))
for element in listche:
    print(element)

new_list = ["banana", "orange", "kiwi", "apple"]
list_1 = [fruit for fruit in new_list if len(fruit) % 2 == 0]
print(list_1)