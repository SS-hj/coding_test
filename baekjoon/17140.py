from collections import Counter
arr = [[0]*100 for _ in range(100)]
R, C, K = map(int, input().split())
for i in range(3):
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())
t = 0
lr, lc = 3, 3

while arr[R-1][C-1] != K:
    t += 1
    if t>100:
        t = -1
        break
    if lr >= lc:
        rows = [[arr[r][c] for c in range(lc) if arr[r][c]] for r in range(lr)]
        arr = [[0]*100 for _ in range(100)]
        for r in range(lr):
            d = Counter(rows[r]).most_common()
            d.sort(key = lambda x : (x[1], x[0]))
            c = 0
            lc = max(lc, len(d)*2)
            for a, b in d:
                arr[r][c] = a
                arr[r][c+1] = b
                c += 2
                if c == 100:
                    break
    else:
        cols = [[arr[r][c] for r in range(lr) if arr[r][c]] for c in range(lc)]
        arr = [[0]*100 for _ in range(100)]
        for c in range(lc):
            d = Counter(cols[c]).most_common()
            d.sort(key = lambda x : (x[1], x[0]))
            r = 0
            lr = max(lr, len(d)*2)
            for a, b in d:
                arr[r][c] = a
                arr[r+1][c] = b
                r += 2
                if r == 100:
                    break
print(t)