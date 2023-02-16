import math
def solution(n, stations, w):
    start = 0
    cnt = 0
    for i in range(len(stations)):
        end = stations[i] - w - 2
        if end >= start:
            cnt += math.ceil((end-start+1)/(2*w+1))
        start = stations[i] + w
    end = n - 1
    if n - 1 >= start:
        cnt += math.ceil((end-start+1)/(2*w+1))
    return cnt