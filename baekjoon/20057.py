n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [0,1,0,-1]
dc = [-1,0,1,0]
total = 0

def tornado(sr,sc,r,c,d):
    global total
    right, left = (d+1)%4, (d-1+4)%4
    ar, ac = r+dr[d], c+dc[d]
    check = [(sr+dr[right],sc+dc[right],0.01),
             (sr+dr[left],sc+dc[left],0.01),
             (r+dr[right],c+dc[right],0.07),
             (r+dr[left],c+dc[left],0.07),
             (r+dr[right]*2,c+dc[right]*2,0.02),
             (r+dr[left]*2,c+dc[left]*2,0.02),
             (ar+dr[right],ac+dc[right],0.1),
             (ar+dr[left],ac+dc[left],0.1),
             (ar+dr[d],ac+dc[d],0.05)]
    temp = 0
    for x,y,z in check:
        temp += int(arr[r][c]*z)
        if 0<=x<n and 0<=y<n:
            arr[x][y] += int(arr[r][c]*z)
        else:
            total += int(arr[r][c]*z)
    if 0<=ar<n and 0<=ac<n:
        arr[ar][ac] += (arr[r][c]-temp)
    else:
        total += (arr[r][c]-temp)
    arr[r][c] = 0

d = 0
r, c = n//2, n//2
for i in range(1,n):
    for _ in range(2):
        # i칸씩 이동
        for _ in range(i):
            nr, nc = r+dr[d], c+dc[d]
            tornado(r,c,nr,nc,d)
            r, c = nr, nc
        d = (d+1)%4
# 마지막 n-1칸을 이동
for _ in range(n-1):
    nr, nc = r+dr[d], c+dc[d]
    tornado(r,c,nr,nc,d)
    r, c = nr, nc
    
print(total)