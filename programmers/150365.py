from collections import deque
def solution(n, m, x, y, r, c, k):
    direct = {'l':(0,-1), 'r':(0,1), 'u':(-1,0), 'd':(1,0)}
    q = deque([(x-1,y-1,"",0)])
    while q:
        i, j, v, cnt = q.popleft()
        if cnt==k and i==r-1 and j==c-1:
            return v
        for d in 'dlru':
            nr, nc = i+direct[d][0], j+direct[d][1]
            if 0<=nr<n and 0<=nc<m and abs(nr-r+1) + abs(nc-c+1) + cnt + 1 <= k:
                q.append((nr,nc,v+d,cnt+1))
                break
    return "impossible"