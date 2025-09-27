list_of_strings = input().split()
number_to_remove = int(input())

list_of_integers = [int(x) for x in list_of_strings]
smallest_numbers = sorted(list_of_integers)[:number_to_remove]

for num in smallest_numbers:
    list_of_integers.remove(num)

print(", ".join(map(str, list_of_integers)))