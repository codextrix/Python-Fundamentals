s1, s2 = input().split()

min_len = min(len(s1), len(s2))

total = sum(ord(s1[i]) * ord(s2[i]) for i in range(min_len))
total += sum(ord(c) for c in s1[min_len:])
total += sum(ord(c) for c in s2[min_len:])

print(total)