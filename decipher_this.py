secret_message = [word for word in input().split()]
deciphered = []

for word in secret_message:
    digits = ""
    for ch in word:
        if ch.isdigit():
            digits += ch
        else:
            break

    first_letter = chr(int(digits))
    rest = word[len(digits):]

    if len(rest) > 1:
        rest = rest[-1] + rest[1:-1]+rest[0]

    deciphered_word = first_letter + rest
    deciphered.append(deciphered_word)


print(" ".join(deciphered))

# first_word = secret_message[0]
# second_word = secret_message[1]
# third_word = secret_message[2]
#
# first_letter = chr(first_word[:1])
# first_word[:1] = first_letter
# first_word[1], first_word[-1] = first_word[-1],first_word[1]
#
