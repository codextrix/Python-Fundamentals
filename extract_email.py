import re
string = input()

pattern = r"(?<!\S)[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@(?:[A-Za-z]+(?:-[A-Za-z]+)*\.)+[A-Za-z]+"

matches = re.findall(pattern, string)

for email in matches:
    print(email)