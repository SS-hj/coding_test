n, m = map(int, input().split())
graph = [[1e9]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a!=k and k!=b:
                graph[a][b] = min(graph[a][k]+graph[k][b], graph[a][b])
            
res = 1e9
for a in range(n):
    res = min(res, graph[a][a])
if res == 1e9:
    print(-1)
else:
    print(res)