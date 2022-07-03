from collections import deque

M,N,H = map(int,input().split())
arr = []
tomato_idx = []
for i in range(H):
    two_arr=[]
    for j in range(N):
        temp = list(map(int,input().split()))
        for k in range(M):
            if temp[k] == 1:
                tomato_idx.append([i,j,k])
        two_arr.append(temp)
    arr.append(two_arr)
dist = [[[0]*M for _ in range(N)] for _ in range(H)]

dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

def bfs():
    q = deque()
    for t in tomato_idx:
        i,j,k = t
        q.append((i,j,k))
        arr[i][j][k] = 1
    while q:
        h, r, c = q.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]
            if 0<=nr<N and 0<=nc<M and 0<=nh<H:
                if arr[nh][nr][nc] == 0:
                    q.append((nh,nr,nc))
                    arr[nh][nr][nc] = 1
                    dist[nh][nr][nc] = dist[h][r][c] + 1
bfs()
check = True
ans = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                check = False
                break
            else:
                ans = max(ans, dist[h][i][j])  # 주의 !! 이렇게 결과를 구해야함
        if not check:
            break
    if not check:
        break
if check:
    print(ans)
else:
    print(-1)