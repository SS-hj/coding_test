from collections import deque

n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = set()

q = deque() 
q.append((0,0,1,False))
visited.add((0,0, False))

while q:
    r, c, d, checked = q.popleft()
    if r== n-1 and c == m-1:
        print(d)
        break
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and (nr,nc,checked) not in visited and not (arr[nr][nc] and checked):
            if arr[nr][nc]:
                q.append((nr,nc,d+1,True))
                visited.add((nr,nc,True))
            else:
                q.append((nr,nc,d+1,checked))
                visited.add((nr,nc,checked))

else:
    print(-1)