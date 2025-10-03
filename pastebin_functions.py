# 1
def find_smallest_number(numbers: list) -> int:
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = find_smallest_number([first_number, second_number, third_number])
print(smallest_number)


# 2
def sum_numbers(first: int, second: int) -> int:
    return first + second


def subtract(some_result: int, third: int) -> int:
    return some_result - third


def add_and_subtract(first_integer: int, second_integer: int, third_integer: int) -> int:
    returned_result = sum_numbers(first_integer, second_integer)
    final_result = subtract(returned_result, third_integer)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)


# 3

def all_the_symbols(first: str, second: str) -> list:
    collected_symbols = []
    for current_symbol_as_integer in range(ord(first) + 1, ord(second)):
        collected_symbols.append(chr(current_symbol_as_integer))
    return collected_symbols


first_character = input()
second_character = input()
symbols = all_the_symbols(first_character, second_character)
print(" ".join(symbols))


# 4

def odd_even_sum(some_number: str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


number = input()
print(odd_even_sum(number))


# 5.1

def is_even(number: int) -> bool:
    return number % 2 == 0


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
result = list(filter(is_even, numbers_as_digits))
print(result)


# 5.2

def is_even(number: int) -> bool:
    return number % 2 == 0


numbers_as_string = input().split()
result = []
for current_number in numbers_as_string:
    if is_even(int(current_number)):  # if is_even(current_number) == True
        result.append(int(current_number))
print(result)

# 5.3

print([int(number) for number in input().split() if int(number) % 2 == 0])


# 8
def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]


numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))


# 9
def check_length(some_password):
    if 6 <= len(some_password) <= 10:
        return True
    return "Password must be between 6 and 10 characters"


def check_letters_and_digits(some_password):
    if some_password.isalnum():
        return True
    return "Password must consist only of letters and digits"


def check_two_digits(some_password):
    digits_counter = 0
    for symbol in some_password:
        if symbol.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    return "Password must have at least 2 digits"


def validate_password(some_password: str) -> list:
    is_valid = []
    is_valid.append(check_length(some_password))
    is_valid.append(check_letters_and_digits(some_password))
    is_valid.append(check_two_digits(some_password))
    for index in range(len(is_valid) - 1, -1, -1):
        if isinstance(is_valid[index], bool):
            is_valid.pop(index)
    return is_valid


password = input()
password_is_not_valid = validate_password(password)
if password_is_not_valid:
    print("\n".join(password_is_not_valid))
else:
    print("Password is valid")


# 10

def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))


# 11

def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percents = some_number // 10
    not_loaded_percent = 10 - loaded_percents
    return f"{some_number}% [" \
           f"{'%' * loaded_percents}" \
           f"{'.' * not_loaded_percent}" \
           "]" \
           f"\nStill loading..."


number = int(input())
print(loading_bar(number))


# 12

def calculate_factorial(number: int) -> int:
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
print(f"{first_factorial / second_factorial:.2f}")