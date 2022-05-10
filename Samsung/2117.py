from collections import deque
'''
----입력
N; 도시 크기 (5 ≤ N ≤ 20)
M; 한 집당 지불할 수 있는 비용 (1 ≤ M ≤ 10)
N*N 크기의 도시정보 ; 집이 있는 위치는 1이고, 나머지는 0 ; 최소 1개 이상의 집이 존재
----출력
price ; K * K + (K - 1) * (K - 1) ; 운영비용 ; 서비스 영역의 면적과 동일
cnt ; 홈방범 서비스를 제공 받는 집들의 수
'''
''' 전체 흐름
    가능한 마름모 생성 (k)
    price 계산
    cnt 계산 ; 해당 마름모내에 있는 집들 count
    if (price-cnt*M->=0):
        count = max(count,-)
'''
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
PLst = [k*k+(k-1)*(k-1) for k in range(22)]     # !!K의 값 리스트 미리 구해놓기!!

def bfs(x, y):
    global maxCnt
    visited = [[0] * N for _ in range(N)]   # !! visited 방문처리 !!
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))

    k = 1
    cnt = graph[x][y]
    if cnt * M - PLst[k] >= 0:
        maxCnt = max(maxCnt, cnt)
    while k < N+1:
        qlen = len(queue)
        for _ in range(qlen):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        if graph[nx][ny]:
                            cnt += 1
        if cnt * M - PLst[k+1] >= 0:
            maxCnt = max(maxCnt, cnt)
        k += 1

for t in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    maxCnt = 0
    # 가능한 모든 그래프의 x 와 y에 대해서 count 계산 (max 를 유지)
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    print('#' + str(t), maxCnt)
