import sys
input=sys.stdin.readline
from collections import deque

node = int(input())
edge = int(input())

# 0이 N+1개인 리스트가 N+1개 만큼 생성됨
# 인덱스가 0부터 시작하기 때문에, 이 부분은 사용하지 않고, 1부터 N+1까지를 실질적으로 사용
graph = [[0] * (node + 1) for _ in range(node + 1)]
visited = [False]*(node+1)

for _ in range(edge):
  x, y = map(int, input().split())
  graph[x][y] = 1

# 너비 우선 탐색
def bfs(start_v):
    visited[start_v] = True # 방문처리 (dfs에서 True 바꾸었기 때문에, 이쪽에서는 False로 처리)
    queue = deque()
    queue.append(start_v)
    while queue:
        v = queue.popleft() # 선입선출
        for w in range(1,node+1):
            if graph[v][w] == 1 and not visited[w]:
                queue.append(w)
                visited[w] = True
            if graph[w][v] == 1 and not visited[w]:
                queue.append(w)
                visited[w] = True
    return sum(visited)-1
       
print(bfs(1))