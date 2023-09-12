n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
visited = {arr[0][0]}
maxDist = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r, c, d):
    global maxDist
    maxDist = max(maxDist, d)
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc] not in visited:
            visited.add(arr[nr][nc])
            dfs(nr,nc,d+1)
            visited.remove(arr[nr][nc])
            
dfs(0,0,1)

print(maxDist)