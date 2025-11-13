import re

import re

pattern = r"(www\.[A-Za-z0-9-]+(?:\.[a-z]+)+)"

links = []

while True:
    try:
        line = input()
    except EOFError:
        break

    matches = re.findall(pattern, line)
    links.extend(matches)

for link in links:
    print(link)
