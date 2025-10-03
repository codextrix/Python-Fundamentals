def sum_numbers(num1, num2) -> int:
    return num1 + num2


def subtract(number_result, number3) -> int:
    return number_result - number3


def add_and_subtract(first_int:int,second_int:int,third_int:int):
    sum_result = sum_numbers(first_int,second_int)
    result = subtract(sum_result,third_int)
    return result

first = int(input())
second = int(input())
third = int(input())

final_result = add_and_subtract(first,second,third)
print(final_result)
