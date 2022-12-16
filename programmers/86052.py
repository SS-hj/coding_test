def solution(grid):
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    res = []
    visited = set()
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        for j in range(m):
            for k in range(4):
                cnt = 0
                while not (i,j,k) in visited:
                    visited.add((i,j,k))
                    if grid[i][j]=="L":
                        k = (k-1)%4
                    elif grid[i][j]=="R":
                        k = (k+1)%4
                    i,j,k = (i+d[k][0])%n,(j+d[k][1])%m, k
                    cnt += 1
                if cnt:
                    res.append(cnt)
    return sorted(res)