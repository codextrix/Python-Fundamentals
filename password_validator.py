def check_length(some_password: str):
    if not 6 <= len(some_password) <= 10:
        return "Password must be between 6 and 10 characters"

def check_letters_and_digits(some_password: str):
    if not some_password.isalnum():
        return "Password must consist only of letters and digits"

def check_two_digits(some_password: str):
    digits_counter = 0
    for symbol in some_password:
        if symbol.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        return "Password must have at least 2 digits"

def validate_password(some_password: str) -> list[str]:
    errors = []
    for check in (check_length, check_letters_and_digits, check_two_digits):
        result = check(some_password)
        if result:   # only add messages, skip None
            errors.append(result)
    return errors


password = input()
validation_errors = validate_password(password)

if not validation_errors:
    print("Password is valid")
else:
    print("\n".join(validation_errors))
