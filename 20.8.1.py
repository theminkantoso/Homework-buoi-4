s = 'ThiS is String with Upper and lower case Letters'

# Or see Python's Counter class: counts = Counter(s.lower())
counts = {}
for c in s.lower():
    counts[c] = counts.get(c, 0) + 1

for c, n in sorted(counts.items()):
    print(c, n)