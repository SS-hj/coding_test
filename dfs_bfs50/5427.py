from collections import deque

T = int(input())

for t in range(T):
    m, n = map(int, input().split())
    graph = []

    for i in range(n):
        graph.append(list(input()))
        if '@' in graph[i]:
            q = deque([(0, i, graph[i].index('@'))])

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                q.append((-1, i, j)) 
    # 다른 종류의 bfs를 구분할 수 있도록 0, -1로 각각 할당
    # 이때 time == -1인 경우에는 불이므로 시간을 업데이트 하지 않음

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 'IMPOSSIBLE'

    while q:
        time, x, y = q.popleft()

        # 탈출
        if time > -1 and graph[x][y] != '*' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
            ans = time + 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':

                # 이동
                if time > -1 and graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    q.append((time + 1, nx, ny)) # time + 1로 누적 시간 계산

                # 불 퍼뜨리기
                elif time == -1 and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    q.append((-1, nx, ny))

    print(ans)