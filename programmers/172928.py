def solution(park, routes):
    move = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    n, m = len(park), len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=='S':
                r, c = i,j
    for route in routes:
        d, step = route.split()
        dr, dc = move[d]
        nr, nc = r, c
        for _ in range(int(step)):
            nr, nc = nr+dr, nc+dc
            if not (0<=nr<n and 0<=nc<m) or park[nr][nc]=='X':
                break
        else:
            r, c = nr, nc
    return [r, c]