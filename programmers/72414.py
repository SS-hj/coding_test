import heapq
def solution(play_time, adv_time, logs):
    c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
    n = c(play_time)
    arr = [0]*n
    q_start = []
    q_end = []
    for log in logs:
        start, end = log.split("-")
        heapq.heappush(q_start,(c(start),c(end)))
    start, end = 0, c(adv_time)-1
    maxSum = 0
    k = 0
    for i in range(n):
        while q_start and i==q_start[0][0]:
            heapq.heappush(q_end, heapq.heappop(q_start)[1]-1)
        arr[i] = len(q_end)
        while q_end and i==q_end[0]:
            heapq.heappop(q_end)
        if i<end:
            maxSum += arr[i]
        elif i==end:
            maxSum += arr[i]
            nowSum = maxSum
        else:
            nowSum += arr[i]
            nowSum -= arr[i-end-1]
            if maxSum < nowSum:
                k = i-end
                maxSum = nowSum
    start += k
    return f"{start//3600:02d}:{(start%3600)//60:02d}:{start%60:02d}"