def solution(n, computers):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    def dfs(r,c):
        visited[r][c] = True
        for i in range(n):
            if not visited[r][i] and computers[r][i]:
                visited[r][i] = True
                dfs(i,r)
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j]:
                dfs(i,j)
                cnt += 1
    return cnt