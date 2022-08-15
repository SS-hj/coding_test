def solution(info, edges):
    visited = [False]*len(info)
    visited[0] = True
    ans = []
    def dfs(sheep, wolf):
        if sheep > wolf:
            ans.append(sheep)
        else: return
        for i in range(len(edges)):
            parent,child = edges[i]
            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep+(info[child]==0),wolf+(info[child]==1))
                visited[child] = False
    dfs(1,0)
    return max(ans)