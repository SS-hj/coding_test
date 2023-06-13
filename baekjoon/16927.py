from collections import deque
n, m, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
minr,maxr,minc,maxc = 0,n,0,m

def move(minr,maxr,minc,maxc):
    global arr
    q = deque()
    for c in range(minc,maxc):
        q.append(arr[minr][c])
    for r in range(minr+1,maxr):
        q.append(arr[r][maxc-1])
    for c in range(maxc-2,minc-1,-1):
        q.append(arr[maxr-1][c])
    for r in range(maxr-2,minr,-1):
        q.append(arr[r][minc])
        
    for _ in range(R%len(q)):
        q.append(q.popleft())
        
    for c in range(minc,maxc):
        arr[minr][c] = q.popleft()
    for r in range(minr+1,maxr):
        arr[r][maxc-1] = q.popleft()
    for c in range(maxc-2,minc-1,-1):
        arr[maxr-1][c] = q.popleft()
    for r in range(maxr-2,minr,-1):
        arr[r][minc] = q.popleft()
    
while minr<maxr and minc<maxc:
    move(minr,maxr,minc,maxc)
    minr,maxr,minc,maxc = minr+1,maxr-1,minc+1,maxc-1
    
for r in range(n):
    print(*arr[r])