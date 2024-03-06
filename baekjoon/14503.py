n, m = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]
cnt = 0

while True:
    if arr[r][c]==0:
        arr[r][c] = 2
        cnt += 1
    for i in range(1,5):
        nr, nc = r+dr[(d-i)%4], c+dc[(d-i)%4]
        if 0<=nr<n and 0<=nc<m and not arr[nr][nc]:
            r, c, d = nr, nc, (d-i)%4
            break
    else:   # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        nr, nc = r+dr[(d-2)%4], c+dc[(d-2)%4]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc]!=1:
            r, c = nr, nc
        else:
            break

print(cnt)