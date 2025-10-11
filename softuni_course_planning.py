schedule = input().split(", ")

while True:
    command = input().strip()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        lesson = parts[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson, idx = parts[1], int(parts[2])
        if lesson not in schedule:
            schedule.insert(idx, lesson)

    elif action == "Remove":
        lesson = parts[1]
        ex = f"{lesson}-Exercise"
        if lesson in schedule:
            schedule.remove(lesson)
        if ex in schedule:
            schedule.remove(ex)

    elif action == "Swap":
        l1, l2 = parts[1], parts[2]
        if l1 in schedule and l2 in schedule:
            i1, i2 = schedule.index(l1), schedule.index(l2)
            schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

            # keep exercises immediately after their lesson
            for l in (l1, l2):
                ex = f"{l}-Exercise"
                if ex in schedule:
                    schedule.remove(ex)
                    li = schedule.index(l)
                    schedule.insert(li + 1, ex)

    elif action == "Exercise":
        lesson = parts[1]
        ex = f"{lesson}-Exercise"
        if lesson in schedule:
            if ex not in schedule:
                li = schedule.index(lesson)
                schedule.insert(li + 1, ex)
        else:
            schedule.append(lesson)
            schedule.append(ex)

for i, title in enumerate(schedule, start=1):
    print(f"{i}.{title}")
