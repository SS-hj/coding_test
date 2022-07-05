from collections import deque

T = int(input())

dr = [-2,-2,2,2,1,-1,1,-1]
dc = [1,-1,1,-1,-2,-2,2,2]

def bfs(sx,sy,fx,fy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    end = False
    while q:
        if end:
            break
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if nr == fx and nc == fy:
                    dist[nr][nc] = dist[r][c] + 1
                    end = True
                    break
                q.append((nr,nc))
                visited[nr][nc] = True
                dist[nr][nc] = dist[r][c] + 1
                
for t in range(T):
    n = int(input())
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    visited = [[False]*n for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    
    bfs(sx,sy,fx,fy)   
    print(dist[fx][fy])