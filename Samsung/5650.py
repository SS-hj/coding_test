T = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 블록의 수직면을 만나면 반대방향으로 돌아감
# 경사면을 만나면 직각으로 꺽여 나감
change_dir = ((), # dummy
               # 1
              (3, 0, 1, 2), # 2
              (2, 0, 3, 1), # 3
              (1, 2, 3, 0),
              (1, 3, 0, 2),# 4
              (1, 0, 3, 2)) # 5

def game(r, c, d):  # dfs 사용
    global wormhole_info
    score = 0
    sr, sc = r, c
    while True:
        r += dx[d]
        c += dy[d]
        # 게임 종료 조건
        # 1. 블랙홀(-1)을 만나면  2. 출발위치로 돌아오면
        if board[r][c] == -1 or (r, c) == (sr, sc):
            return score
        if 1 <= board[r][c] <= 5:
            d = change_dir[board[r][c]][d]
            score += 1
        if 6 <= board[r][c] <= 10:
            r, c = wormhole_info[(r, c)]

for t in range(1, T + 1):
    n = int(input())
    maxScore = float('-inf')
    wormhole_check = [0] * 11
    wormhole_info = dict()
    board = [[5] * (n + 2)]  # !! 맵 벽(5)으로 둘러싸기 !!
    for r in range(1,n+1):
        board.append([5] + list(map(int, input().split())) + [5])
        for c in range(1,n+1):
            if 6 <= board[r][c] <= 10:
                num = board[r][c]
                if not wormhole_check[num]: # 처음 추가하는 웜홀일 경우
                    wormhole_check[num] = (r, c)
                else:  # 같은 번호 웜홀끼리 위치 정보 저장
                    # 처음 추가한 웜홀 인덱스에 새로운 웜홀 인덱스 저장
                    wormhole_info[wormhole_check[num]] = (r, c)
                    # 새로운 웜홀 인덱스에 처음 추가한 웜홀 인덱스 저장
                    wormhole_info[(r, c)] = wormhole_check[num]
    board.append([5] * (n + 2))
    # 모든 출발위치와 진행방향을 전부 탐색
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j] == 0:
                for k in range(4):
                    maxScore = max(maxScore, game(i, j, k))
    print("#" + str(t), maxScore)
