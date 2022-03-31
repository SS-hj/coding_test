import sys
input=sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [False]*(n+1)

for i in range(n):
    for k in range(m):
        graph[i][k] = int(graph[i][k])

# 가능한 모든 길을 탐색하고 그 중 가장 짧은 길을 묻는 문제에는 bfs 가 더 적합
# 너비 우선 탐색

# 동서남북 방향 (서동남북)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 방문처리 (탐색했으므로 저장)
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 동서남북 방향으로 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우, 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 현재까지의 이동 거리 + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))