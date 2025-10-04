import math


def get_distance(x1_, y1_, x2_, y2_):
    point1 = (int(x1_), int(y1_))
    point2 = (int(x2_), int(y2_))

    result1 = abs(x1_) + abs(y1_)
    result2 = abs(x2_) + abs(y2_)

    if result1 <= result2:
        return point1
    else:
        return point2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(get_distance(x1, y1, x2, y2))
