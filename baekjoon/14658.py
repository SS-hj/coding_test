N, M, L, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
rows = list(r for r,_ in arr)
cols = list(c for _,c in arr)

maxCnt = 0
for sr in rows:
    for sc in cols:
        er, ec = sr+L, sc+L
        cnt = 0
        for r, c in arr:
            if sr<=r<=er and sc<=c<=ec:
                cnt += 1
        maxCnt = max(maxCnt, cnt)
    
print(K-maxCnt)