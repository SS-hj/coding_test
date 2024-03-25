n, m, x, y, _ = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
d = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]
dice = [0] * 6
roll = [[0, 1, 5, 4, 2, 3], [0, 1, 4, 5, 3, 2], [4, 5, 2, 3, 1, 0], [5, 4, 2, 3, 0, 1]]

for i in orders:
    nx, ny = x+d[i][0],y+d[i][1]
    if 0<=nx<n and 0<=ny<m:
        # 주사위 굴리기
        dice = [dice[r] for r in roll[i-1]]
        # 조건에 따른 복사
        if arr[nx][ny]==0:
            arr[nx][ny] = dice[5]
        else:
            dice[5] = arr[nx][ny]
            arr[nx][ny] = 0
        x, y = nx, ny
        print(dice[4])