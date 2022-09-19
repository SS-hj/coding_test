d = [[0] for _ in range(12)]
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4,12):
    d[i] = d[i-1] + d[i-2] + d[i-3]

T = int(input())
for t in range(T):
    print(d[int(input())])