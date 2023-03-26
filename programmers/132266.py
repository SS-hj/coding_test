from collections import deque
def solution(n, roads, sources, destination):
    adj = [[] for _ in range(n+1)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    dist = [-1]*(n+1)
    dist[destination] = 0
    q = deque([destination])
    while q:
        x = q.popleft()
        for nx in adj[x]:
            if dist[nx]==-1:
                dist[nx] = dist[x]+1
                q.append(nx)
    return [dist[i] for i in sources]