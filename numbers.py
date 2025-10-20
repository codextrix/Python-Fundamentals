integers = list(map(int, input().split()))
average_sum = sum(integers) / len(integers)

greater_than_average = [num for num in integers if num > average_sum]

if greater_than_average:
    top_five = sorted(greater_than_average, reverse=True)
    if len(top_five) > 5:
        print(" ".join(map(str, top_five[:5])))
    else:
        print(" ".join(map(str, top_five[:5])))
else:
    print("No")