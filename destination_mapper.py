import re

text = input()

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"

destinations = []
travel_points = 0

matches = re.finditer(pattern, text)

for match in matches:
    destination = match.group(2)
    destinations.append(destination)
    travel_points += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
