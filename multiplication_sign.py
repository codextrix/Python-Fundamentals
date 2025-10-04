num1 = int(input())
num2 = int(input())
num3 = int(input())


def multiplication_sign(number1, number2, number3) -> str:
    """
    Takes three number,checks the sign and counts it if the count of the negative numbers is odd
    :param number1:
    :param number2:
    :param number3:
    :return:
    """
    numbers = [number1,number2, number3]
    odd_counter = 0
    for num in numbers:
        if num == 0:
            return "zero"
        if num < 0:
            odd_counter += 1

    if odd_counter % 2 == 0:
        return "positive"
    else:
        return "negative"


print(multiplication_sign(num1, num2, num3))
