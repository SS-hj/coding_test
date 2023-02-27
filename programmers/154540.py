from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        maps[i] = list(maps[i])
    res = []
    visited = [[False]*m for _ in range(n)]

    def bfs(sr,sc,d):
        q = deque()
        q.append((sr,sc))
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                    if maps[nr][nc] != "X":
                        d += int(maps[nr][nc])
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return d

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != "X":
                visited[i][j] = True
                res.append(bfs(i,j,int(maps[i][j])))

    return sorted(res) if res else [-1]