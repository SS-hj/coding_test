from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)] # 방문처리를 해줘야 시간초과 방지

dr = [1, 0]
dc = [0, 1]

ans = 'Hing'

queue = deque()
queue.append((0,0))
    
while queue:
    x, y = queue.popleft()
    step = graph[x][y]
    if step == -1:
        ans = 'HaruHaru'
        break
    for i in range(2):
        nx = x + step*dr[i]
        ny = y + step*dc[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            queue.append((nx,ny))
            visited[nx][ny] = True
print(ans)