from copy import deepcopy

R, C, M = map(int, input().split())

dr = [-1,1,0,0]
dc = [0,0,1,-1]
fisher = -1
temp = []
phase1 = [[[0,0,0]]*C for _ in range(R)]
phase2 = [[[0,0,0]]*C for _ in range(R)]
res = 0

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    phase1[r-1][c-1] = [s,d-1,z]
    if c-1 == fisher+1: # 다음에 낚시꾼이 낚을 수 있는 열에 있으면
        if temp and temp[0] < r-1:
            continue
        temp = [r-1,z]  # temp가 없거나, 더 가까우면 업데이트

def reverseDirect(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2
def index(nr,nc,d):
    if 0<=nr<R and 0<=nc<C:
        return nr, nc, d
    else:
        while not 0<=nr<R:
            if nr>=R:
                nr = R-1-(nr-(R-1)) if nr >= R else nr
            else:
                nr *= -1
            # 방향을 반대로 바꿔주기
            d = reverseDirect(d)
        while not 0<=nc<C:
            if nc>=C:
                nc = C-1-(nc-(C-1)) if nc >= C else nc
            else:
                nc *= -1
            # 방향을 반대로 바꿔주기
            d = reverseDirect(d)
        return nr, nc, d

for _ in range(C):
    fisher += 1
    if temp:
        res += temp[1]
        phase1[temp[0]][fisher] = [0,0,0]
    temp = []
    for r in range(R):
        for c in range(C):
            s,d,z = phase1[r][c]
            if z==0:
                continue
            nr, nc, d = index(r+dr[d]*s, c+dc[d]*s, d)
            if phase2[nr][nc][2] >= z:          # 이미 해당 자리에 더 큰 상어가 있으면
                continue
            else:
                phase2[nr][nc] = [s, d, z]
            if nc == fisher + 1:                # 다음에 낚시꾼이 낚을 수 있는 열에 있으면
                if temp and temp[0] < nr:
                    continue
                temp = [nr, phase2[nr][nc][2]]  # temp가 없거나, 더 가까우면 업데이트
    phase1 = deepcopy(phase2)
    phase2 = [[[0,0,0]]*C for _ in range(R)]

print(res)