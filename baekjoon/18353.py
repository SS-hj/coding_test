import heapq
n = int(input())
arr = list(map(int, input().split()))
h = []
for i in range(n-1, -1, -1):
    temp = []
    while h:
        cnt, num = heapq.heappop(h)
        temp.append((cnt, num))
        if num < arr[i]:
            heapq.heappush(h, (cnt-1, arr[i]))
            break
    else:
        heapq.heappush(h, (-1, arr[i]))

    for cnt, num in temp:
        heapq.heappush(h, (cnt, num))

cnt, num = heapq.heappop(h)
print(n+cnt)