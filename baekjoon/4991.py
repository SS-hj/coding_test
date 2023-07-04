from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(sr,sc,er,ec):
    visited = set()
    q = deque([(sr,sc,0)])
    while q:
        r,c,d = q.popleft()
        if r==er and c==ec:
            return d
        for i in range(4):
            nr, nc = r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited and arr[nr][nc]!="x":
                visited.add((nr,nc))
                q.append((nr,nc,d+1))

while True:
    m, n = map(int,input().split())
    if m==0:
        break
    arr = []
    dirty = []
    for r in range(n):
        temp = list(input().rstrip())
        for c in range(m):
            if temp[c]=="o":
                sr, sc = r, c
            elif temp[c]=="*":
                dirty.append((r,c))
        arr.append(temp)
    is_possible = True
    fromstart = []
    for er,ec in dirty:
        d = bfs(sr,sc,er,ec)
        if not d:
            print(-1)
            is_possible = False
            break
        fromstart.append(d)
        
    if is_possible:
        minD = 1e9
        k = len(dirty)
        dist = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(i+1,k):
                dist[i][j] = bfs(*dirty[i],*dirty[j])
                dist[j][i] = dist[i][j]
        for perm in permutations(range(k)):
            x = perm[0]
            d = fromstart[x]
            for nx in perm[1:]:
                d += dist[x][nx]
                x = nx
            minD = min(minD, d)
        print(minD)