n = input()
digits = list(n)

digits.sort(reverse=False)
largest = "".join(digits)
print(largest)