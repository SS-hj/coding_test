from collections import deque

m, n = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            q.append((i,j))
            arr[i][j] = 1
while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0:
            q.append((nr,nc))
            arr[nr][nc] = 1
            dist[nr][nc] = dist[r][c] + 1
            
check = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            check = True
            
if check:
    print(-1)
else:
    print(max(map(max,dist)))