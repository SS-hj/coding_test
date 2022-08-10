from collections import deque
def solution(n, edge):
    dist = [0]*(n+1)
    # 양방향 그래프 트리 생성
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        u, v = e[0], e[1]
        adj[u].append(v)
        adj[v].append(u)
    q = deque(); maxD = 0
    q.append((1,1))
    while q:
        pn, d = q.popleft()
        if not dist[pn]:
            dist[pn] = d
            for e in adj[pn]: # 트리와 연결 되어있는 다음 노드로
                q.append((e, d+1))
            maxD = max(maxD,d)
    return dist.count(maxD)