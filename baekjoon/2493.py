import heapq
n = int(input())
arr = list(map(int,input().split()))

res = [0]*n
h = []
for i in range(n-1,-1,-1):
    while h and h[0][0] <= arr[i]:
        res[heapq.heappop(h)[1]] = i+1
    heapq.heappush(h, (arr[i], i))

print(*res)