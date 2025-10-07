numbers = [int(number) for number in input().split(", ")]

even = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even)