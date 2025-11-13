import re

string = input()
word = input()

pattern = rf"\b{re.escape(word)}\b"
matches = re.findall(pattern, string, flags=re.IGNORECASE)


print(len(matches))
