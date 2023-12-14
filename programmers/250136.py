from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    res = [0]*m
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    visited = [[0]*m for _ in range(n)]
    check = {}
    v = 1
    for j in range(m):
        cnt = 0
        temp = set()
        for i in range(n):
            # 석유가 있고, 해당 열에서 이미 처리한 석유덩어리가 아닌 경우
            if land[i][j] and visited[i][j] not in temp:
                # 이전에 방문한 적이 있는 경우
                if visited[i][j]>0:
                    temp.add(visited[i][j])
                    cnt += check[visited[i][j]]
                # 처음 탐색하는 경우 bfs
                else:
                    q = deque([(i,j)])
                    visited[i][j] = v
                    dist = 1
                    while q:
                        r, c = q.popleft()
                        for d in range(4):
                            nr, nc = r+dr[d], c+dc[d]
                            if 0<=nr<n and 0<=nc<m and land[nr][nc] and not visited[nr][nc]:
                                q.append((nr,nc))
                                visited[nr][nc] = v
                                dist += 1
                    check[v] = dist
                    cnt += check[v]
                    temp.add(v)
                    v += 1
        res[j] = cnt
    return max(res)