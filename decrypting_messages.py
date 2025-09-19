key = int(input())
lines = int(input())
message = ""

for line in range(lines):
    letter = input()
    message += chr(ord(letter) + key)

print(message)



