import re

text = input()
calories = 0

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1([1-9][0-9]{0,4})\1"
matches = re.findall(pattern, text)

for match in matches:
    calories += int(match[3])

days = calories // 2000

print(f"You have food to last you for: {days} days!")

for match in matches:
    item = match[1]
    date = match[2]
    nutr = match[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {nutr}")
