import re

encrypted_message = input()
pattern = r"([*^]+)([A-Za-z ]{6,})([*^]+)([^A-Za-z0-9]*?)\+([-]?\d+(?:\.\d+)?,[-]?\d+(?:\.\d+)?)\++"

found = False

for match in re.finditer(pattern, encrypted_message):
        found = True
        artifakt = match.group(2)
        coordinates = match.group(5)
        print(f"Found {artifakt} at coordinates {coordinates}.")

if not found:
    print("No valid artifacts found.")