from collections import defaultdict
T = int(input())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 튜플로 인덱싱하여 처리할 수 있는 경우, 이렇게 하도록. (좀 더 효율적? & 깔끔)
change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))

for t in range(T):
    n = int(input())
    arr = [[5]*(n+2)]
    wormhole = defaultdict(list)
    for r in range(n):
        temp = list(map(int, input().split()))
        for c in range(n):
            if 6<=temp[c]<=10:
                wormhole[temp[c]].append((r+1,c+1))
        arr.append([5]+temp+[5])
    arr.append([5]*(n+2))
    maxScore = 0
    for r in range(1,n+1):
        for c in range(1,n+1):
            if arr[r][c]==0:
                for d in range(4):
                    start = (r,c)
                    nr, nc = r+dr[d],c+dc[d]
                    score = 0
                    while (nr,nc)!=start and arr[nr][nc]!=-1:   # 출발지점으로 돌아오거나, 블랙홀에 빠진 경우 게임 종료
                        if 1<=arr[nr][nc]<=5:                   # 블록에 만난 경우, 방향 바뀜 (벽도 함께 처리)
                            d = change_dir[arr[nr][nc]][d]
                            score += 1
                        elif 6<=arr[nr][nc]<=10:                # 웜홀에 빠진 경우
                            a, b = wormhole[arr[nr][nc]]
                            if a==(nr, nc):
                                nr, nc = b
                            else:
                                nr, nc = a
                        nr, nc = nr+dr[d],nc+dc[d]
                    maxScore = max(maxScore, score)

    print(f"#{t+1} {maxScore}")