def all_the_symbols(first,second) -> list:
    collected = []
    for current_symbol in range(ord(first)+1, ord(second)):
        collected.append(chr(current_symbol))
    return collected


chr1 = input()
chr2 = input()
symbols = all_the_symbols(chr1,chr2)
print(" ".join(symbols))