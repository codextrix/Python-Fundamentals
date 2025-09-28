field = [list(map(int, input().split())) for _ in range(3)]

winner = 0

for row in field:
    if row[0] == row[1] == row[2] != 0:
        winner = row[0]

for col in range(3):
    if field[0][col] == field[1][col] == field[2][col] != 0:
        winner = field[0][col]

if field[0][0] == field[1][1] == field[2][2] != 0:
    winner = field[0][0]
if field[0][2] == field[1][1] == field[2][0] != 0:
    winner = field[0][2]

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")