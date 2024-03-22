from collections import deque
n, k = map(int, input().split())
q = deque()
visited = [100001]*100001
q.append((n, 0))
visited[n] = 0
res = 1e9

while q:
    now, d = q.popleft()
    if now==k:
        res = min(res, d)
    else:
        if 0 <= now*2 < 100001 and visited[now*2]>d:
            visited[now*2] = d
            q.append((now*2, d))
        if 0 <= now+1 < 100001 and visited[now+1]>d+1:
            visited[now+1] = d+1
            q.append((now+1, d+1))
        if 0 <= now-1 < 100001 and visited[now-1]>d+1:
            visited[now-1] = d+1
            q.append((now-1, d+1))

print(res)