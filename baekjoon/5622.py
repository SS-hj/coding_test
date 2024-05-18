temp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
d = {}
for i in range(len(temp)):
    for s in temp[i]:
        d[s] = i+3

print(sum(d[s] for s in input()))