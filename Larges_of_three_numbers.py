num1 = int(input())
num2 = int(input())
num3 = int(input())

largest = 0

if num1 > num2:
    largest = num1
else:
    largest = num2

if num3 > largest:
    largest = num3

print(largest)


# num1, num2, num3 = int(input()), int(input()), int(input())
#
# large = max(num1,num2, num3)
# print(large)