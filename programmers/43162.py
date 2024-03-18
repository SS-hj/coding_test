def solution(n, computers):
    visited = [False]*n
    cnt = 0
    def dfs(node):
        visited[node] = True
        for nxt in range(n):
            if computers[node][nxt] and not visited[nxt]:
                dfs(nxt)
    for i in range(n):
        for j in range(i,n):
            if computers[i][j] and not visited[j]:
                dfs(j)
                cnt += 1
    return cnt