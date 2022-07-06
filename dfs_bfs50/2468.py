from collections import deque

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
maxv = max(map(max, arr))
res = []

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc):
    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if check[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = True

check = [[0]*n for _ in range(n)]              
for t in range(0, maxv+1):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and arr[i][j] <= t:
                check[i][j] = 1
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    res.append(cnt)

print(max(res))