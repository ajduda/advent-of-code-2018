file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

records = []

for line in z.split('\n'):
    records.append(line)

#Get the lines in order. Conveneiently ordered timestamp such that a regular sort does that for me
records.sort()

guardSleepTimeMinutes = {}

for record in records:
    words = record.split(" ")
    minute = int(words[1].split(":")[1][:-1])
    if words[2] == "Guard":
        guard = int(words[3][1:])  # Ignore the # for the guard number
        if guard not in guardSleepTimeMinutes:
            guardSleepTimeMinutes[guard] = []
            for i in range(60):
                guardSleepTimeMinutes[guard].append(0)
    if words[2] == "falls":
        sleepTime = minute
    if words[2] == "wakes":
        for i in range(sleepTime,minute):
            guardSleepTimeMinutes[guard][i] += 1

maxGuard = -1
maxSleptTime = -1
maxMinuteID = -1

for guard in guardSleepTimeMinutes:
    for minute in range(60):
        sleptTime = guardSleepTimeMinutes[guard][minute]
        if sleptTime > maxSleptTime:
            maxSleptTime = sleptTime
            maxGuard = guard
            maxMinuteID = minute

print(maxMinuteID * maxGuard)