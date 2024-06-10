from collections import deque

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
input()
heights = list(map(int, input().split()))
check = [[] for _ in range(R)]
dr = [0,0,-1,1]
dc = [-1,1,0,0]
q = deque()
cluster = set()
def boom(d, r):
    if d==0:
        c = 0
        while c<C:
            if arr[r][c]=="x":
                arr[r][c]="."
                return c
            c += 1
    else:
        c = C-1
        while c>=0:
            if arr[r][c]=="x":
                arr[r][c]="."
                return c
            c -= 1
    return -1

for idx, height in enumerate(heights):
    y = R-height
    x = boom(idx%2, y)
    
    if x>=0:
        visited = set()
        for i in range(4):
            nr, nc = y+dr[i],x+dc[i]
            if 0<=nr<R and 0<=nc<C and arr[nr][nc]=="x" and (nr,nc) not in visited:
                q.append((nr,nc))
                cluster.add((nr,nc))
                visited.add((nr,nc))
            while q:
                r, c = q.popleft()
                if r==R-1:
                    q = deque()
                    cluster = set()
                    break   # 새로 생긴 클러스터가 땅에 붙은 경우
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<=nr<R and 0<=nc<C and arr[nr][nc]=="x" and ((nr,nc)) not in cluster:
                        q.append((nr,nc))
                        cluster.add((nr,nc))
                        visited.add((nr,nc))
            if cluster: # 새로 생긴 클러스터가 떠 있는 경우
                checked = False
                for r, c in cluster:
                    arr[r][c] = "."
                for diff in range(2, R):
                    for r, c in cluster:
                        if r+diff == R or arr[r+diff][c]=="x":
                            checked = True
                            break
                    if checked:
                        break
                while cluster:
                    r, c = cluster.pop()
                    arr[r+diff-1][c] = "x"
                break
            
for r in range(R):
    print("".join(arr[r]))