# def is_even(num:int) -> bool:
#     return num % 2 == 0
#
#
# numbers_string = input().split()
#
# numbers = [int(number) for number in numbers_string]
# result = list(filter(is_even, numbers))
# print(result)


def is_even(num:int) -> bool:
    return num % 2 == 0


numbers_string = input().split()
numbers = [int(number) for number in numbers_string]
result = []
for current_number in numbers:
     if is_even(current_number):
        result.append(current_number)

print(result)