students = []

while True:
    line = input().strip()
    if ":" not in line:
        target_course = line.replace("_", " ")
        break
    name, sid, course = line.split(":")
    students.append((name, sid, course))

for name, sid, course in students:
    if course == target_course:
        print(f"{name} - {sid}")
