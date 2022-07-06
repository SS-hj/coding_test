from collections import deque

F, S, E, U, D = map(int,input().split())
arr = list(range(F+1))
dist = [0] * (F+1)

dx = [U, -D]
q = deque()
q.append(S)
res = "use the stairs"

while q:
    x = q.popleft()
    if x == E:
        res = dist[x]
        break
    for i in range(2):
        nx = x + dx[i]
        if 1<=nx<=F and nx != S and dist[nx] == 0:
            q.append(nx)
            dist[nx] = dist[x] + 1
                
print(res)