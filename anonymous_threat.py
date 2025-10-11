def merge(some_list:list, current_command:list) -> list:
    start_index, end_index = int(current_command[1]), int(current_command[2])

    # clamp indexes to valid bounds
    if start_index < 0:
        start_index = 0
    if end_index >= len(some_list):
        end_index = len(some_list) - 1
    if start_index > end_index:
        return some_list

    # end must be inclusive -> end_index + 1
    some_list[start_index] = "".join(some_list[start_index:end_index + 1])
    # keep everything before start, then the merged, then everything after end
    some_list = some_list[:start_index + 1] + some_list[end_index + 1:]
    return some_list


def divide(some_list:list, current_command:list) -> list:
    index, partitions = int(current_command[1]), int(current_command[2])
    if partitions <= 0:
        return some_list

    element = some_list[index]
    partition_size = len(element) // partitions
    partitioned_elements = []
    number_of_partition = 0
    current_index = 0  # reuse this name instead of a step-based range (avoids step=0 issue)

    # make all except the last equal length; last is the longest
    while number_of_partition < partitions:
        number_of_partition += 1
        if number_of_partition == partitions:
            current_partitions = element[current_index:]
        else:
            current_partitions = element[current_index:current_index + partition_size]
            current_index += partition_size
        partitioned_elements.append(current_partitions)

    some_list = some_list[:index] + partitioned_elements + some_list[index+1:]
    return some_list


input_line = input().split()
command = input()
while command != "3:1":
    command = command.split()
    action = command[0]

    if action == "merge":
        input_line = merge(input_line, command)
    elif action == "divide":
        input_line = divide(input_line, command)

    command = input()

print(" ".join(input_line))
