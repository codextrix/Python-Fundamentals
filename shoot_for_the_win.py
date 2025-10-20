seq_int = list(map(int, input().split(" ")))
shots = 0
command = input()

while command != "End":
    index = int(command)

    if 0 <= index < len(seq_int) and seq_int[index] != -1:
        shot_value = seq_int[index]
        seq_int[index] = -1
        shots += 1

        for i in range(len(seq_int)):
            if seq_int[i] == -1:
                continue
            if seq_int[i] > shot_value:
                seq_int[i] -= shot_value
            else:
                seq_int[i] += shot_value
    command = input()

joined = " ".join(map(str, seq_int))
print(f"Shot targets: {shots} -> {joined}")
