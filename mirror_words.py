import re

words_string = input()

pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = list(re.finditer(pattern, words_string))
mirror_words = []

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

for match in matches:
    first_word = match.group(2)
    second_word = match.group(3)
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
