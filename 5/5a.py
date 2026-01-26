file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

# We can just remove as we go, greedy algorithm works great here

stack = []

for c in z:
    n = ord(c)

    # The difference between an upper and lowercase letter is a single bit
    if len(stack) > 0 and stack[-1] ^ n == 32:
        stack.pop()
    else:
        stack.append(n)
    
print(len(stack))
