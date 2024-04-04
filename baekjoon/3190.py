from collections import deque
n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 2
l = int(input())
change = [] # a초뒤, 방향 바꿈
for _ in range(l):
    a, b = input().split()
    if b=='D':
        change.append([int(a), 1])
    else:
        change.append([int(a),-1])
dr = [0,1,0,-1]
dc = [1,0,-1,0]
p, d, t = 0, 0, 0
r, c = 0,0
arr[0][0] = 1
snake = deque([(0,0)])
while True:
    t += 1
    nr, nc = r+dr[d], c+dc[d]
    if not (0<=nr<n and 0<=nc<n) or arr[nr][nc]==1:
        print(t)
        break
    elif arr[nr][nc]!=2:
        r, c = snake.popleft()
        arr[r][c] = 0
    arr[nr][nc] = 1
    snake.append((nr,nc))
    r,c = nr,nc
    if p<l and t==change[p][0]:
        d = (d+change[p][1]+4)%4
        p += 1