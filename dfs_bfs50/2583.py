from collections import deque

m, n, k = map(int,input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    r1,c1,r2,c2 = map(int,input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            arr[i][j] = 1
visited = [[False]*m for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                if not visited[nr][nc] and arr[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    cnt += 1
    return cnt

cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 0:
            r = bfs(i,j)
            cnt += 1
            res.append(r)

print(cnt)
res.sort()
for i in res:
    print(i, end= ' ')