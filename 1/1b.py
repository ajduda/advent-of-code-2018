file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

numbers = []

for line in z.split('\n'):
    numbers.append(int(line))


seen = {0}
total = 0
i = 0

while True:
    total += numbers[i]
    if total in seen:
        print(total)
        exit()
    seen.add(total)
    i += 1
    if i == len(numbers):
        i = 0
