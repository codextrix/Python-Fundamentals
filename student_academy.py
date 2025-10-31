n = int(input())

grades = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name, gs in grades.items():
    avg = sum(gs) / len(gs)
    if avg >= 4.50:
        print(f"{name} -> {avg:.2f}")
