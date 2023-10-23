from collections import deque
def solution(maps):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q = deque([(0,0,1)])
    visited = set([(0,0)])
    n, m = len(maps), len(maps[0])
    while q:
        r, c, d = q.popleft()
        if r==n-1 and c==m-1:
            return d
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc,d+1))
    return -1