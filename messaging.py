numbers_string = input().split(" ")
chars = list(input().rstrip())

numbers = [int(nums) for nums in numbers_string]
message = []

for num in numbers:
    sum_of_digits = sum(map(int, str(num)))
    index = sum_of_digits % len(chars)
    chr = chars.pop(index)      
    message.append(chr)

print("".join(message))
