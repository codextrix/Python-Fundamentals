def add_stop(stops_, index_, string_):
    if 0<= index_ <= len(stops_):
        before = stops_[:index_]
        after = stops_[index_:]
        new_stops = before + string_ + after
        return new_stops
    return stops_

def remove_stop(stops_, start_index_, end_index_):
    if 0<= start_index_ <= end_index_ <= len(stops_):
        before = stops_[:start_index_]
        after = stops_[end_index_+1:]
        new_stops = before + after
        return new_stops
    return stops_

def switch(stops_, old_sting_, new_string_):
    if old_sting_ in stops_:
        new_stops = stops_.replace(old_sting_, new_string_)
        return new_stops
    return stops_


stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        stops  =add_stop(stops, index, string)
        print(stops)

    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove_stop(stops, start_index, end_index)
        print(stops)

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        stops = switch(stops, old_string, new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")

