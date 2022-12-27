import heapq
def solution(n, works):
    h = []
    res = 0
    for work in works:
        heapq.heappush(h,-work)
    for _ in range(n):
        temp = heapq.heappop(h)
        if temp:
            heapq.heappush(h,temp+1)
        else:
            return 0
    while h:
        res += heapq.heappop(h)**2
    return res