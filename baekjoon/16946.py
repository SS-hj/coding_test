import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
group = [[0]*m for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
k = 1
check = {0:0}

for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and group[i][j]==0:
            q = deque([(i,j)])
            group[i][j] = k
            cnt = 1
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0 and group[nr][nc]==0:
                        group[nr][nc] = k
                        q.append((nr,nc))
                        cnt += 1
            check[k] = cnt
            k += 1

for r in range(n):
    for c in range(m):
        if arr[r][c]:
            gg = set()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<n and 0<=nc<m:
                    gg.add(group[nr][nc])
            for g in gg:
                arr[r][c] += check[g]
            arr[r][c] %= 10

for a in arr:
    print("".join(map(str,a)))