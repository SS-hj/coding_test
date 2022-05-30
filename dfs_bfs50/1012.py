import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        r, c = queue.popleft() # 선입선출
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < n) and (0 <= nc < m):
                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    queue.append((nr,nc))

T = int(input())

for t in range(T):
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            # 처음 1을 발견할 때 bfs 를 수행하고 
            # 처리되는 노드들을 0으로 바꾸면서
            # bfs 수행 횟수를 카운트하면 1로 이루어진 그룹 개수를 구할 수 있다.
            if graph[a][b] == 1: 
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
                