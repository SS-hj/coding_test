n = int(input())
arr = [[0]*101 for _ in range(101)]
dr = [0,-1,0,1]
dc = [1,0,-1,0]

# draw dragon curve
for _ in range(n):
    c,r,d,g = map(int,input().split())
    arr[r][c] = 1
    stack = [d] # 방향들 append
    r, c = r+dr[d], c+dc[d]
    arr[r][c] = 1
    for _ in range(g):
        temp = stack[:]
        while temp:
            # 이전 방향의 90도 반시계 방향으로 그려야 드래곤 커브가 그려짐
            d = (temp.pop()+1)%4
            r, c = r+dr[d], c+dc[d]
            arr[r][c] = 1
            stack.append(d)
            
# count squares
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]==arr[i][j+1]==arr[i+1][j]==arr[i+1][j+1]==1:
            cnt += 1

print(cnt)