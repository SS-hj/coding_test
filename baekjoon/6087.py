from collections import deque

m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]
q = deque()
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "C":
            if not q:
                for d in range(4):
                    q.append((i,j,d,0))
                arr[i][j] = 0
            else:
                er, ec = i, j
                arr[i][j] = 1e9
        elif arr[i][j]==".":
            arr[i][j] = 1e9

while q:
    r, c, d, k = q.popleft()
    # 90도 회전한 방향은 +1 or -1
    nd = (d+3)%4
    nr, nc = r+dr[nd], c+dc[nd]
    while 0<=nr<n and 0<=nc<m and arr[nr][nc]!="*":
        if arr[nr][nc] > k:
            arr[nr][nc] = k
            q.append((nr,nc,nd,k+1))
        nr, nc = nr+dr[nd], nc+dc[nd]
    nd = (d+1)%4
    nr, nc = r+dr[nd], c+dc[nd]
    while 0<=nr<n and 0<=nc<m and arr[nr][nc]!="*":
        if arr[nr][nc] > k:
            arr[nr][nc] = k
            q.append((nr,nc,nd,k+1))
        nr, nc = nr+dr[nd], nc+dc[nd]

print(arr[er][ec])