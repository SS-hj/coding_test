import sys
input=sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
# 0이 N+1개인 리스트가 N+1개 만큼 생성됨
# 인덱스가 0부터 시작하기 때문에, 이 부분은 사용하지 않고, 1부터 N+1까지를 실질적으로 사용
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False]*(N+1)

for _ in range(M):
  x, y = map(int, input().split())
  # 노드 연결 하기 (양방향 이므로 x->y와 y->x 둘 다 연결)
  graph[x][y] = graph[y][x] = 1

# 깊이 우선 탐색
def dfs(start_v):
  visited[start_v] = True # 방문처리
  print(start_v, end=' ')
  for w in range(1, N+1):
    # 현재 노드와 인접한 방문하지 않은 다른 노드 재귀적으로 방문
    if graph[start_v][w] == 1 and not visited[w]:
        dfs(w) # 재귀 함수

# 너비 우선 탐색
def bfs(start_v):
  visited[start_v] = False # 방문처리 (dfs에서 True 바꾸었기 때문에, 이쪽에서는 False로 처리)
  queue = deque()
  queue.append(start_v)
  while queue:
    v = queue.popleft() # 선입선출
    print(v, end=' ')
    for w in range(1,N+1):
      if graph[v][w] == 1 and visited[w]:
        queue.append(w)
        visited[w] = False

dfs(V)
print() # 한 줄 띄우기
bfs(V)