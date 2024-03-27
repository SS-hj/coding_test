from collections import deque
n, m , t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rot = [-1, 1] # 시계방향으로, 반시계 방향으로
# 상하좌우로 인접 (특히, 좌우의 경우 범위 상관X)
dr = [-1,1,0,0]
dc = [0,0,-1,1]
q = deque()
for _ in range(t):
    x, d, k = map(int, input().split())
    # 1. rotation: xi의 배수인 원판을 di방향으로 ki칸 회전
    for i in range(x-1,n,x):
        arr[i] = arr[i][k*rot[d]:]+arr[i][:(m+k*rot[d])%m]
    checked = False
    total = []
    index = []
    for v in range(n):
        for w in range(m):
            if arr[v][w]:   # 지움 처리가 안된 경우
                total.append(arr[v][w])
                index.append((v,w))
                q.append((v,w))
                num = arr[v][w]
                # 인접하면서 같은 수 모두 지움
                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        nr, nc = r+dr[i], (c+dc[i])%m
                        if 0<=nr<n and arr[nr][nc] and arr[nr][nc]==num:
                            arr[nr][nc] = 0
                            checked = True
                            q.append((nr,nc))
    # 인접한 수가 하나도 지워지지 않았다면 원판의 평균 구하여 process
    if not checked and total:
        mean = sum(total)/len(total)
        for r,c in index:
            if arr[r][c]>mean:
                arr[r][c]-=1
            elif arr[r][c]<mean:
                arr[r][c]+=1
                
print(sum(arr[r][c] for r,c in index))