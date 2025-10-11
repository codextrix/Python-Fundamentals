old_version = input().split(".")
n1, n2, n3 = map(int, old_version)

n3 += 1
if n3 > 9:
    n3 = 0
    n2 +=1
    if n2 > 9:
        n2 = 0
        n1 += 1

print(f"{n1}.{n2}.{n3}")

# first = old_version[0]
# second = old_version[1]
# third = old_version[2]
#
# if int(third) < 9:
#     new = int(third) + 1
#     print(".".join(first, second, new))