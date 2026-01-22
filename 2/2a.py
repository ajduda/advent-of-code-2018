file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

twos = 0
threes = 0

for line in z.split('\n'):
    letterCounts = {}
    for c in line:
        if c not in letterCounts:
            letterCounts[c] = 1
        else:
            letterCounts[c] += 1
    counts = letterCounts.values()
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1


print(twos * threes)