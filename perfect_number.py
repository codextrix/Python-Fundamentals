def is_perfect(num:int)-> int:
    divisors_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor

    if divisors_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(is_perfect(number))