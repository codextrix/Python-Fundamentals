def swap(current_array, current_index1, current_index2):
    current_array[current_index1], current_array[current_index2] = \
        current_array[current_index2], current_array[current_index1]
    return current_array


def multiply(current_array, current_index1, current_index2):
    current_array[current_index1] = current_array[current_index1] * current_array[current_index2]
    return current_array


def decrease(current_array):
    return [x - 1 for x in current_array]


array_int = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "swap":
        index1, index2 = int(command[1]), int(command[2])
        array_int = swap(array_int, index1, index2)

    elif command[0] == "multiply":
        index1, index2 = int(command[1]), int(command[2])
        array_int = multiply(array_int, index1, index2)

    elif command[0] == "decrease":
        array_int = decrease(array_int)

print(", ".join(map(str, array_int)))
