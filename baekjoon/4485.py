import sys
input = sys.stdin.readline
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

t = 0
while True:
    t += 1
    n = int(input())
    if n<=0:
        break
    arr = [list(map(int,input().split())) for _ in range(n)]
    q = deque()
    q.append((0,0))
    dist = [[1e9]*n for _ in range(n)]
    dist[0][0] = arr[0][0]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<n and dist[r][c]+arr[nr][nc]<dist[nr][nc]:
                dist[nr][nc] = dist[r][c]+arr[nr][nc]
                q.append((nr,nc))
    print(f'Problem {t}: {dist[n-1][n-1]}')