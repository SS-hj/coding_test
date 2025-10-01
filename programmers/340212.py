def solution(diffs, times, limit):
    start, end = 1, min(max(diffs), limit)
    times.append(0)
    while start < end:
        mid = (start+end)//2
        total = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total += times[i]
            else:
                total += ((diffs[i] - mid)*(times[i]+times[i-1])+times[i])
            if total > limit:
                start = mid+1
                break
        else:
            end = mid
    
    return end