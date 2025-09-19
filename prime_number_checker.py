from sympy import isprime
number = int(input())
prime = isprime(number)
print(prime)

num = int(input())

# if num > 1:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     print(is_prime)
# else:
#     print(False)
