file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

# Keeping a set of every point with cloth on it
# Not scalable for a bigger problem but this will work for day 3 numbers
cloth = set()
overlap = set()

for line in z.split('\n'):
    l,r = line.split(" @ ")
    id = l[1:]
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
                overlap.add((x,y))
            cloth.add((x,y))


print(len(overlap))