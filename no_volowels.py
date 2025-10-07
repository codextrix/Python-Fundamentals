word = input()

sorted_list = [char for char in word if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(sorted_list))