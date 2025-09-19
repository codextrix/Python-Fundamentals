lines = int(input())
last = ""
balanced = True
for line in range(lines):
    bracket_string = input()
    if bracket_string == "(":
        if last == "(":
            balanced = False
            break
        last = "("
    elif bracket_string == ")":
        if last == ")":
            balanced = False
            break
        last = ")"
    else:
        continue

if last == "(":
    balanced = False

if balanced is True:
    print("BALANCED")
else:
    print("UNBALANCED")
