def solution(mats, park):
    mats.sort(reverse=True)
    n, m = len(park), len(park[0])

    maxN = -1
    for i in range(n):
        for j in range(m):
            if park[i][j]!="-1":
                park[i][j] = 0
            else:
                park[i][j] = -1

    for i in range(n):
        for j in range(m):
            if park[i][j]==-1:
                for k in mats:
                    if k <= maxN:
                        break
                    if i+k<=n and j+k<=m and sum(sum(row[j:j+k]) for row in park[i:i+k])==-k*k:
                        maxN = max(maxN, k)
    for m in mats:
        if maxN >= m:
            return m
    else:
        return -1