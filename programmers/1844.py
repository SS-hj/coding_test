from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    dist[0][0] = 1
    answer = -1
    while(q):
        r, c = q.popleft()
        if r == n-1 and c == m-1:
            answer = dist[r][c]
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if maps[nr][nc] == 1:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1
    return answer