number_of_electrons = int(input())

shell = []
current_shell = 1

while number_of_electrons > 0:
    electrons_needed = 2 * (current_shell ** 2)
    if number_of_electrons > electrons_needed:
        shell.append(electrons_needed)
        number_of_electrons -= electrons_needed
    else:
        shell.append(number_of_electrons)
        break
    current_shell += 1

print(shell)