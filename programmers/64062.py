def solution(stones, k):
    left = 1; right = max(stones)
    while left <= right:
        cnt = 0
        mid = (right + left) // 2 # 징검다리를 건널 수 있는 수 
        for stone in stones:
            if stone - mid <= 0: cnt += 1
            else: cnt = 0
            if cnt >= k:
                right = mid - 1
                break
        else:
            left = mid + 1
    return left