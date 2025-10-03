def calcilate_factorial(number:int) -> int:
    for current_number in range(1,number):
        number *= current_number

    return number


first = int(input())
second = int(input())
first_factorial = calcilate_factorial(first)
second_factorial = calcilate_factorial(second)
print(f"{first_factorial / second_factorial:.2f}")