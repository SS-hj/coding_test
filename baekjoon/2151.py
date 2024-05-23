from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]
direct = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == "#":
            sr = i
            sc = j
            break

# 각 방향마다 최소 visit 수로
visited = [[[1e9,1e9,1e9,1e9] for _ in range(n)] for _ in range(n)]
q = deque([])

for i in range(4):
    visited[sr][sc][i] = 0
    q.append((sr,sc,0,i))

while q:
    r, c, dist, d = q.popleft()
    nr = r + direct[d][0]
    nc = c + direct[d][1]
    if 0<=nr<n and 0<=nc<n and arr[nr][nc] != "*" and visited[nr][nc][d]>dist:
        if arr[nr][nc] == "#":
            print(dist)
            break
        
        # 해당 방향 그대로 가는 것부터 탐색하도록 (최소 거울 수를 탐색하기 위해)
        q.appendleft((nr,nc,dist,d))
        visited[nr][nc][d] = dist

        if arr[nr][nc] == "!":
            # 좌우 90도 방향만
            q.append((nr,nc,dist+1,(d+3)%4))
            q.append((nr,nc,dist+1,(d+1)%4))