first_sting = input()
second_string = input()

for character_index in range(len(first_sting)):
    left = second_string[:character_index + 1]
    right = first_sting[character_index + 1:]
    if first_sting[character_index] != second_string[character_index]:
        print(left + right)