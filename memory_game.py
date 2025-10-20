def main():
    sequence = input().split()
    moves = 0

    while True:
        line = input().strip()
        if line == "end":
            break

        i_str, j_str = line.split()
        first_idx, second_idx = int(i_str), int(j_str)
        moves += 1

        # invalid move: same index or out of bounds
        if (
            first_idx == second_idx
            or first_idx < 0 or second_idx < 0
            or first_idx >= len(sequence) or second_idx >= len(sequence)
        ):
            print("Invalid input! Adding additional elements to the board")
            to_add = f"-{moves}a"
            middle = len(sequence) // 2
            sequence.insert(middle, to_add)
            sequence.insert(middle, to_add)
            continue

        # valid indices -> check for match
        if sequence[first_idx] == sequence[second_idx]:
            element = sequence[first_idx]
            print(f"Congrats! You have found matching elements - {element}!")
            # remove by indices (delete higher index first)
            for idx in sorted((first_idx, second_idx), reverse=True):
                sequence.pop(idx)
            if not sequence:
                print(f"You have won in {moves} turns!")
                return
        else:
            print("Try again!")

    print("Sorry you lose :(")
    print(" ".join(sequence))


if __name__ == "__main__":
    main()
