import heapq
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : (-x[0], -x[1]))

maxDay = arr[0][0]
arr = deque(arr)
h = []
res = 0

for d in range(maxDay,0,-1):
    while arr and arr[0][0] >= d:
        day, score = arr.popleft()
        heapq.heappush(h, -score)
    if h:
        res -= heapq.heappop(h)
        
print(res)