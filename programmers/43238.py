def solution(n, times):
    start, end = 0, times[0]*n
    while start<=end:
        mid = (start+end)//2
        person = 0
        for time in times:
            person += mid//time
            if person>=n:
                res = mid
                end = mid-1
                break
        else:
            start = mid+1
    return res