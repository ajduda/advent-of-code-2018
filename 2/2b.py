file = 'test.txt'
file = 'input.txt'

with open(file) as inp:
    z = inp.read()
    z = z.strip()

twos = 0
threes = 0

IDs = z.split('\n')

for i in range(len(IDs)):
    ID1 = IDs[i]
    for j in range(i+1,len(IDs)):
        ID2 = IDs[j]
        wrong = 0
        for k in range(len(ID1)):
            if ID1[k] != ID2[k]:
                wrong += 1
            if wrong > 1:
                break
        if wrong == 1:
            ans = ""
            for k in range(len(ID1)):
                if ID1[k] == ID2[k]:
                    ans += ID1[k]
            print(ans)
            exit()

print("No answers were found")