from collections import deque

n, m = map(int, input().split())
a = dict()
for _ in range(n+m):
	x, y = map(int, input().split())
	a[x-1] = y-1
q = deque()
q.append((0, 0))
visited = [False]*100
visited[0] = True
while q:
	now, n = q.popleft()
	if now == 99:
		print(n)
		break
	for k in range(1, 7):
		nxt = now + k
		nr, nc = nxt//10, nxt%10
		if 0<=nr<10 and 0<=nc<10:
			if nxt in a:
				nxt = a[nxt]
			if not visited[nxt]:
				visited[nxt] = True
				q.append((nxt, n+1))