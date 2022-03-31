import sys
input=sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [False]*(n+1)

for i in range(n):
    for k in range(n):
        graph[i][k] = int(graph[i][k])

# 동서남북 방향 (서동남북)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 큐 사용
    graph[x][y] = 0 # 재방문하지 않도록 방문처리
    cnt = 1
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 동서남북 방향으로 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 해당 노드를 처음 방문하는 경우, 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문처리
                queue.append((nx,ny))
                cnt += 1 # 이동거리 카운트
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(i, j))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])