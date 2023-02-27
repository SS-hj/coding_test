import heapq
def solution(jobs):
    total = 0
    end = 0
    h = []
    for a, b in jobs:
        heapq.heappush(h, (a, b))
    temp = []
    while h:
        while h and h[0][0] <= end:
            start, time = heapq.heappop(h)
            heapq.heappush(temp, (time, start))
        if not temp:
            end = h[0][0]
            continue
        time, start = heapq.heappop(temp)
        total += end - start + time
        end += time
        while temp:
            time, start = heapq.heappop(temp)
            heapq.heappush(h, (start, time))
    return int(total/len(jobs))


import heapq
def solution(n, times):
    res = []
    for time in times:
        heapq.heappush(res, (time, time))
    maxNum = max(times)
    now = maxNum
    n -= len(times)
    temp = []
    '''
    maxtime을 걸어놓고 
    n>0인 동안 
    가장 작은 값을 더하고 더하고 ... 그렇게 더함
    이렇게 해서 max인 값이 최종 결과값
    '''
    while n > 0:
        while res and res[0][0] < now:
            total, time = heapq.heappop(res)
            heapq.heappush(temp, (time,total))
        while temp and n > 0:
            time, total = heapq.heappop(temp)
            heapq.heappush(res, (total+time,time))
            n -= 1
        now += maxNum
    return max(res)[0]