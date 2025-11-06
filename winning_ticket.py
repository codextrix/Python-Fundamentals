import re

tickets = [t.strip() for t in input().split(",") if t.strip()]

def longest_run(half: str, sym: str) -> int:

    return max((len(m.group(0)) for m in re.finditer(re.escape(sym) + r"+", half)), default=0)

for t in tickets:
    if len(t) != 20:
        print("invalid ticket")
        continue

    left, right = t[:10], t[10:]

    best_len = 0
    best_sym = ""
    for sym in "@#$^":
        l = longest_run(left, sym)
        r = longest_run(right, sym)
        curr = min(l, r)
        if curr > best_len:
            best_len = curr
            best_sym = sym

    if best_len >= 6:
        if best_len == 10:
            print(f'ticket "{t}" - {best_len}{best_sym} Jackpot!')
        else:
            print(f'ticket "{t}" - {best_len}{best_sym}')
    else:
        print(f'ticket "{t}" - no match')
