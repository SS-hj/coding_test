import heapq
def solution(book_time):
    time = []
    res = []
    for start, end in book_time:
        time.append([int(start[:2])*60+int(start[3:]), int(end[:2])*60+int(end[3:])+10])
    for start, end in sorted(time):
        if res and res[0] <= start:
            heapq.heapreplace(res, end)
        else:
            heapq.heappush(res, end)
    return len(res)