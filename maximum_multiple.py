divisor = abs(int(input()))
boundary = abs(int(input()))

largest = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > largest:
            largest = i

print(largest)