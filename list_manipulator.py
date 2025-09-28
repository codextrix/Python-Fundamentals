def is_even (n):
    return n % 2 == 0

numbers = list(map(int, input().split(" ")))

while True:
    command = input()

    if command == "end":
        break

    parts = command.split()

    if parts[0] == "exchange":
        index = int(parts[1])
        if 0 <= index < len(numbers):
            numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")

    elif parts[0] in ["max","min"]:
        even_odd = parts[1]
        if even_odd == "even":
            filtered = [n for n in numbers if is_even(n)]
        else:
            filtered = [n for n in numbers if not is_even(n)]

        if not filtered:
            print("No matches")
        else:
            if parts[0] == "max":
                target = max(filtered)
            else:
                target = min(filtered)

            print(len(numbers) - 1 - numbers[::-1].index(target))

    elif parts[0] in ["first", "last"]:
        count = int(parts[1])
        even_odd = parts[2]

        if count > len(numbers):
            print("Invalid count")
            continue
        if even_odd == "even":
            filtered = [n for n in numbers if is_even(n)]
        else:
            filtered = [n for n in numbers if not is_even(n)]

        if parts[0] == "first":
            print(filtered[:count])
        else:
            print(filtered[-count:])

print(numbers)