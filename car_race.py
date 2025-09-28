numbers_strings = input().split(" ")
numbers_integers = [int(number) for number in numbers_strings]

middle = len(numbers_integers) // 2
left = numbers_integers[:middle]
right = numbers_integers[:middle:-1]

sum_of_numbers_left = 0
sum_of_numbers_right = 0

for numl in left:
    if numl == 0:
        sum_of_numbers_left *= 0.8
    else:
        sum_of_numbers_left += numl

for numr in right:
    if numr == 0:
        sum_of_numbers_right *= 0.8
    else:
        sum_of_numbers_right += numr

if sum_of_numbers_right > sum_of_numbers_left:
    print(f"The winner is left with total time: {sum_of_numbers_left:.1f}")
else:
   print(f"The winner is right with total time: {sum_of_numbers_right:.1f}")