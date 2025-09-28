people = input().split()
step = int(input())
people_integers = [int(number) for number in people]
result = []

index = 0
while people_integers:
    index = (index + step - 1) % len(people_integers)
    result.append(people_integers.pop(index))

print("[" + ",".join(map(str,result)) + "]")