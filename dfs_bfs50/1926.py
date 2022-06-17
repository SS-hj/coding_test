from collections import deque

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

pic = []
def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if arr[nr][nc]:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    cnt += 1
    return cnt
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            pic += [bfs(i,j)]

print(len(pic))
if len(pic) == 0:
    print(0)
else:
    print(max(pic))