from itertools import product
from copy import deepcopy

n, m = map(int, input().split())
res = [[0]*m for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
check = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]
d = [[[0],[1],[2],[3]],[[0,1],[2,3]], [[0,2], [0,3], [1,2], [1,3]], [[0,1,2], [1,2,3], [2,3,0], [3,0,1]]]

total = n*m
for r in range(n):
    for c in range(m):
        if arr[r][c]>0:
            if res[r][c] != '#':
                res[r][c] = '#'
                total -= 1
            if arr[r][c]<5:
                temp = [(arr[r][c], r,c, i) for i in range(len(d[arr[r][c]-1]))]
                check.append(temp)
            elif arr[r][c]==5:
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    while 0<=nr<n and 0<=nc<m and arr[nr][nc]!=6:
                        if res[nr][nc] != '#':
                            res[nr][nc] = '#'
                            total -= 1
                        nr, nc = nr+dr[i], nc+dc[i]
                        
check_list = list(product(*check))

minCnt = n*m
for check in check_list:
    A = deepcopy(res)
    cnt = total
    for k,r,c,x in check:
        direct = d[k-1][x]
        for i in direct:
            nr, nc = r+dr[i], c+dc[i]
            while 0<=nr<n and 0<=nc<m and arr[nr][nc]!=6:
                if A[nr][nc] != '#':
                    A[nr][nc] = '#'
                    cnt -= 1
                nr, nc = nr+dr[i], nc+dc[i]
    minCnt = min(minCnt, cnt)

print(minCnt)