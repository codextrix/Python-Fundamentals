def is_palindrome(num:str) -> bool:

    return num == num[::-1]

numbers = input().split(", ")
for number in numbers:
    print(is_palindrome(number))