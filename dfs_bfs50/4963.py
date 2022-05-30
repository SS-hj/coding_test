import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우 + 대각선
dr = [-1, 1, 0, 0,-1,-1,1,1]
dc = [0, 0, -1, 1,-1,1,-1,1]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        r, c = queue.popleft() # 선입선출
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < h) and (0 <= nc < w):
                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    queue.append((nr,nc))

while True:
    w, h = map(int,input().split())
    if (w,h) == (0,0): break
    graph = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0

    for a in range(h):
        for b in range(w):
            # 처음 1을 발견할 때 bfs 를 수행하고 
            # 처리되는 노드들을 0으로 바꾸면서
            # bfs 수행 횟수를 카운트하면 1로 이루어진 그룹 개수를 구할 수 있다.
            if graph[a][b] == 1: 
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
                