def urgent(current_item):
    if current_item not in initial_list:
        initial_list.insert(0, current_item)
    return initial_list


def unnecessary(current_item):
    if current_item in initial_list:
        initial_list.remove(current_item)
    return initial_list


def correct(curr_old, curr_new):
    if curr_old in initial_list:
        idx = initial_list.index(curr_old)
        initial_list[idx] = curr_new
    return initial_list


def rearrange(current_item):
    if current_item in initial_list:
        initial_list.remove(current_item)
        initial_list.append(current_item)
    return initial_list


initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    action = command.split()
    do = action[0]

    if do == "Urgent":
        item = action[1]
        initial_list = urgent(item)
    elif do == "Unnecessary":
        item = action[1]
        initial_list = unnecessary(item)
    elif do == "Correct":
        old = action[1]
        new = action[2]
        initial_list = correct(old, new)
    elif do == "Rearrange":
        item = action[1]
        initial_list = rearrange(item)

    command = input()

print(", ".join(initial_list))
