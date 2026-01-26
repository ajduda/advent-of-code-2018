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

guardSleepTime = {}
guardSleepTimeMinutes = {}

for record in records:
    words = record.split(" ")
    minute = int(words[1].split(":")[1][:-1])
    if words[2] == "Guard":
        guard = int(words[3][1:])  # Ignore the # for the guard number
        if guard not in guardSleepTime:
            guardSleepTime[guard] = 0
            guardSleepTimeMinutes[guard] = []
            for i in range(60):
                guardSleepTimeMinutes[guard].append(0)
    if words[2] == "falls":
        sleepTime = minute
    if words[2] == "wakes":
        guardSleepTime[guard] += minute - sleepTime
        for i in range(sleepTime,minute):
            guardSleepTimeMinutes[guard][i] += 1

maxSleep = -1
maxGuard = -1
for guard in guardSleepTime:
    if guardSleepTime[guard] > maxSleep:
        maxSleep = guardSleepTime[guard]
        maxGuard = guard

maxMinute = 0

#I don't want this GIANT lookup phrase for the only scheddule that matters, so we reduce it here
minuteSlept = guardSleepTimeMinutes[maxGuard]


for i in range(1,60):
    if minuteSlept[i] > minuteSlept[maxMinute]:
        maxMinute = i

print(maxMinute * maxGuard)