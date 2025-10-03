def smallest(numbers:list):
    return min(numbers)


first = int(input())
second = int(input())
third = int(input())
smallest_number = smallest([first,second,third])

print(smallest_number)