from copy import deepcopy

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

res = 1e9

for r in range(1, n-1):
    for c in range(1,m-1):
        if arr[r][c]=="R":
            red = (r,c)
        elif arr[r][c]=="B":
            blue = (r,c)
        elif arr[r][c]=="O":
            hole = (r,c)

def move(nd, count, A):
    global res
    d = {'R':(0,0), 'B':(0,0)}
    # 0:오른쪽, 1:아래, 2:왼쪽, 3:위
    if nd == 0:
        for r in range(n):
            temp = []
            for c in range(m):
                if A[r][c]=="#":
                    for i in range(c-1,-1,-1):
                        if not temp:
                            break
                        tt = temp.pop()
                        d[tt] = (r,i)
                        A[r][i] = tt
                elif A[r][c]=="R" or A[r][c]=="B":
                    temp.append(A[r][c])
                    A[r][c] = "."
                elif A[r][c]=="O":
                    if "B" in temp:
                        return False
                    elif "R" in temp:
                        res = min(res, count)
                        return False
            for i in range(m-1,-1,-1):
                if not temp:
                    break
                tt = temp.pop()
                d[tt] = (r,i)
                A[r][i] = tt
    elif nd == 1:
        for c in range(m):
            temp = []
            for r in range(n):
                if A[r][c]=="#":
                    for i in range(r-1,-1,-1):
                        if not temp:
                            break
                        tt = temp.pop()
                        d[tt] = (i,c)
                        A[i][c] = tt
                elif A[r][c]=="R" or A[r][c]=="B":
                    temp.append(A[r][c])
                    A[r][c] = "."
                elif A[r][c]=="O":
                    if "B" in temp:
                        return False
                    elif "R" in temp:
                        res = min(res, count)
                        return False
            for i in range(n-1,-1,-1):
                if not temp:
                    break
                tt = temp.pop()
                d[tt] = (i,c)
                A[i][c] = tt
        
    elif nd == 2:
        for r in range(n):
            temp = []
            for c in range(m-1,-1,-1):
                if A[r][c]=="#":
                    for i in range(c+1,m):
                        if not temp:
                            break
                        tt = temp.pop()
                        d[tt] = (r,i)
                        A[r][i] = tt
                elif A[r][c]=="R" or A[r][c]=="B":
                    temp.append(A[r][c])
                    A[r][c] = "."
                elif A[r][c]=="O":
                    if "B" in temp:
                        return False
                    elif "R" in temp:
                        res = min(res, count)
                        return False
            for i in range(m):
                if not temp:
                    break
                tt = temp.pop()
                d[tt] = (r,i)
                A[r][i] = tt
    else:
        for c in range(m):
            temp = []
            for r in range(n-1,-1,-1):
                if A[r][c]=="#":
                    for i in range(r+1,n):
                        if not temp:
                            break
                        tt = temp.pop()
                        d[tt] = (i,c)
                        A[i][c] = tt
                elif A[r][c]=="R" or A[r][c]=="B":
                    temp.append(A[r][c])
                    A[r][c] = "."
                elif A[r][c]=="O":
                    if "B" in temp:
                        return False
                    elif "R" in temp: # blue가 없으면서 red가 있는 경우
                        res = min(res, count)
                        return False
            for i in range(n):
                if not temp:
                    break
                tt = temp.pop()
                d[tt] = (i,c)
                A[i][c] = tt
    return A
    
def dfs(d, count, A):
    if count<res and count<10:
        for i in range(4):
            if d%2!=i%2:
                B = move(i, count+1, deepcopy(A))
                if B:
                    dfs(i, count+1, deepcopy(B))
                
for i in range(4):
    B = move(i, 1, deepcopy(arr))
    if B:
        dfs(i, 1, deepcopy(B))

if res==1e9:
    print(-1)
else:
    print(res)