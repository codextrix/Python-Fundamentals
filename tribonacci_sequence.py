number = int(input())


def tribonacci_sequence(num):
    sequence = [1, 1, 2]
    if num <= 3:
        sequence = sequence[:num]
    else:
        for index in range(3, num):
            next_num = sequence[index - 1] + sequence[index - 2] + sequence[index - 3]
            sequence.append(next_num)
    print(" ".join(str(x) for x in sequence))

tribonacci_sequence(number)