from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def timeFlow(A):
    B = deepcopy(A)
    for r in range(n):
        for c in range(m):
            if A[r][c]==0:
                continue
            cnt = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<n and 0<=nc<m and A[nr][nc]==0:
                   cnt += 1
            B[r][c] = max(A[r][c]-cnt,0)
    return B

def checkGroup():
    cnt = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] and (i,j) not in visited:
                cnt += 1
                q = deque([(i,j)])
                visited.add((i,j))
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr, nc = r+dr[d], c+dc[d]
                        if 0<=nr<n and 0<=nc<m and arr[nr][nc] and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            q.append((nr,nc))     
    return cnt

time = 0
while True:
    time += 1
    arr = timeFlow(arr)
    cnt = checkGroup()
    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(time)
        break