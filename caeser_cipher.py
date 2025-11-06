string = input()
cipher = []
for ch in string:
    cipher.append(chr(ord(ch) + 3))

print("".join(cipher))

