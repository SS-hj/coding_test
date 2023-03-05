def solution(n, s, a, b, fares):
    graph = [[1e9]*n for _ in range(n)] 
    for u, v, f in fares:
        graph[u-1][v-1] = f
        graph[v-1][u-1] = f

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    res = graph[s-1][a-1]+graph[s-1][b-1]
    for k in range(n):
        res = min(res, graph[s-1][k]+graph[k][a-1]+graph[k][b-1])
    return res