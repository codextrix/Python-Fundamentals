symbols = int(input())
for first in range(97, 97 + symbols):
    for second in range(97, 97 + symbols):
        for third in range(97, 97 + symbols):
            print(f"{chr(first)}{chr(second)}{chr(third)}")