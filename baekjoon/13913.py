from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001  # 해당 위치까지 걸리는 시간
check = [0] * 100001    # 이동 경로 히스토리

q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(visited[now])
        # 역으로 경로 찾기
        data = []
        for _ in range(visited[k]+1):
            data.append(now)    # 현재 위치 추가
            now = check[now]    # 이전 위치 받기
        print(' '.join(map(str,data[::-1])))
        break
    for next_node in (now-1, now+1, now*2):
        # 가능한 범위 내 이면서, 방문하지 않았던 경우
        if  0 <= next_node <= 100000 and visited[next_node] == 0:
            visited[next_node] = visited[now] + 1
            q.append(next_node)
            check[next_node] = now  # 다음 이동위치에 현재 이동위치를 기록