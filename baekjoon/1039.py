import sys
from collections import deque
input = sys.stdin.readline
num, k = map(int,input().split())
n = len(str(num))
res = -1
q = deque([(num, 0)])
visited = set([((num, 0))])
while q:
    x, p = q.popleft()
    if p==k:
        res = max(res, x)
        continue
    num = list(str(x))
    for i in range(n-1):
        for j in range(i+1,n):
            if i==0 and num[j]=="0":
                continue
            num[i], num[j] = num[j], num[i]
            nx = int("".join(num))
            if (nx, p+1) not in visited:
                visited.add((nx, p+1))
                q.append((nx, p+1))
            num[i], num[j] = num[j], num[i]
     
print(res)