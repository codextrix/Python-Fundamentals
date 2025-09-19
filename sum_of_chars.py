num_lines = int(input())
total_sum = 0

for line in range(num_lines):
    character = input()
    total_sum += ord(character)

print(f"The sum equals: {total_sum}")
