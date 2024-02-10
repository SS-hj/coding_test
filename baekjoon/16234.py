from collections import deque
n, lower, upper = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dr = [0,0,-1,1]
dc = [-1,1,0,0]
day = 0
check = n*n
q = deque()

def move_check(r,c,g):
    group[r][c] = g
    group_idx = [(r,c)]
    q.append((r,c))
    total = arr[r][c]
    cnt = 1
    # 인구이동 조건 국경선 오픈 
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0<=nr<n and 0<=nc<n and group[nr][nc]==0 and lower<=abs(arr[r][c]-arr[nr][nc])<=upper:
                total += arr[nr][nc]
                cnt += 1
                group[nr][nc] = g
                group_idx.append((nr,nc))
                q.append((nr,nc))
    # 연합 인구이동
    new_citizen_num = total//cnt
    for r,c in group_idx:
        arr[r][c] = new_citizen_num
                    
while True:
    group = [[0]*n for _ in range(n)]
    g = 0
    for i in range(n):
        for j in range(n):
            if group[i][j]==0:
                g += 1
                move_check(i,j,g)
    if g == check:
        break
    day += 1
    
print(day)