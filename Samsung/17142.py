from collections import deque

# 제너레이터를 이용한 조합
def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next
                
n, m = map(int, input().split())
arr = []
virus = []
zeroNum = n*n   # 빈 칸 수
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c]==1:
            zeroNum -= 1
        if temp[c]==2:
            virus.append((r,c,2,0))
            zeroNum -= 1
    arr.append(temp)
    
if zeroNum==0:  # 빈칸이 없는 경우
    print(0)

else:
    check = list(combinations(virus, m))

    mint = zeroNum+1
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    for comb in check:
        visited = set()
        q = deque(comb)
        maxd = 0
        checked = 0
        while q:
            r, c, ttype, d = q.popleft()
            if ttype == 0:
                maxd = max(maxd, d)
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    if arr[nr][nc]==0:      # 바이러스 감염
                        visited.add((nr,nc))
                        q.append((nr,nc,0,d+1))
                        checked += 1
                    elif arr[nr][nc]==2:    # 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함
                        visited.add((nr,nc))
                        q.append((nr,nc,2,d+1))
        if checked==zeroNum:
            mint = min(mint, maxd)
    print(-1 if mint==zeroNum+1 else mint)  # 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
