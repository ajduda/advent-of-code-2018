file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

# Keeping a dict of every point with cloth on it, and what cloths point to it
# Not scalable for a bigger problem but this will work for day 3 numbers
cloth = {}
overlap = set()

for line in z.split('\n'):
    l,r = line.split(" @ ")
    id = l[1:]
    id = int(id)
    l,r = r.split(": ")
    xStart,yStart = l.split(",")
    xStart = int(xStart)
    yStart = int(yStart)
    xLen,yLen = r.split("x")
    xLen = int(xLen)
    yLen = int(yLen)

    for x in range(xStart,xStart+xLen):
        for y in range(yStart,yStart+yLen):
            if (x,y) in cloth:
                cloth[(x,y)].add(id)
                for n in cloth[(x,y)]:
                    overlap.add(n)  # This is doing a LOT of duplicate/useless work, not scalable
            else:
                cloth[(x,y)] = {id}

id = 1
while id < len(overlap) + 2:  # ID isn't zero indexed, plus last cloth could be the missing one
    if id not in overlap:
        print(id)
        exit()
    id += 1

print("ERROR: No non overlapping ID's found")