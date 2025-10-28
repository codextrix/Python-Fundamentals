words = input().split()

counts = {}
lowered = []
for w in words:
    lw = w.lower()
    lowered.append(lw)
    counts[lw] = counts.get(lw, 0) + 1

seen = set()
result = []
for w in lowered:
    if counts[w] % 2 == 1 and w not in seen:
        result.append(w)
        seen.add(w)

print(" ".join(result))
