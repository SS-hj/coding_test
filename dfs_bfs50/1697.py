from collections import deque

N, K = map(int,input().split())
arr = [0]*100001

q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x==K: # 처음부터 동생과 위치가 같은 경우 주의
        print(arr[x])
        break
    check = [x+1, x-1, x*2]
    for i in range(len(check)):
        nx = check[i]
        if 0<=nx<100001:
            if arr[nx]==0:
                arr[nx] = arr[x]+1
                q.append(nx)