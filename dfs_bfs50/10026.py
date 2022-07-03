from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[False]*n for _ in range(n)]

def dfs(x,y):
    col = arr[x][y]
    q = deque()
    visited[x][y] = True
    if arr[x][y] == 'R':
        arr[x][y] = 'G'
    q.append((x,y))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if arr[nr][nc] == col:
                    visited[nr][nc] = True
                    q.append((nr,nc))
                    if arr[nr][nc] == 'R':
                        arr[nr][nc] = 'G'
                    
normal = 0
rg_test = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            normal += 1
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            rg_test += 1
            
print(normal, rg_test)