n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
chess = {}
d_info = [(0,1),(0,-1),(-1,0),(1,0)]
check = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    r, c, d = list(map(int,input().split()))
    chess[i] = [r-1, c-1, d_info[d-1]] # r, c, d
    check[r-1][c-1].append(i)
maxCnt = 1

def play(p, v):
    global maxCnt
    r, c, d = chess[p]
    t = check[r][c].index(p)
    temp = check[r][c][t:]
    nr, nc = r+d[0], c+d[1]
    check[r][c] = check[r][c][:t]
    if v == 0:
        check[nr][nc].extend(temp)
    else:
        check[nr][nc].extend(temp[::-1])
    maxCnt = max(len(check[nr][nc]), maxCnt)
    for x in temp:
        chess[x] = [nr, nc, chess[x][2]]
    
for i in range(1000):
    for p in range(k):
        r, c, d = chess[p]
        nr, nc = r+d[0], c+d[1]
        if not (0<=nr<n and 0<=nc<n) or arr[nr][nc] == 2:   # 바깥 or 파랑
            # 이동방향 역으로
            d = (-d[0], -d[1])
            chess[p] = [r, c, d]
            nr, nc = r+d[0], c+d[1]
            if not (0<=nr<n and 0<=nc<n) or arr[nr][nc] == 2:
                continue
            elif arr[nr][nc] == 0:
                play(p, 0)
            else:
                play(p, 1)
        elif arr[nr][nc] == 0:  # 도착할 칸이 흰
            play(p, 0)
        else:                   # 도착할 칸이 빨강
            play(p, 1)
    if maxCnt >= 4:
        print(i+1)
        break
else:
    print(-1) # 게임이 1000번 이상 종료되지 않는 경우
                  